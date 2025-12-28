# Overview: VictoriaLogs в Kubernetes

## Введение

**VictoriaLogs** — это высокопроизводительное хранилище логов от команды VictoriaMetrics, оптимизированное для больших объёмов данных, с низким потреблением ресурсов и простотой эксплуатации. В Kubernetes VictoriaLogs органично вписывается в экосистему observability и может использоваться как централизованное хранилище логов для приложений, ingress-контроллеров и событий безопасности.

В этой статье мы рассмотрим:

* архитектуру VictoriaLogs в Kubernetes,
* установку через Helm,
* интеграцию с cert-manager и ingress,
* генерацию логов и метрик,
* пример практического сценария с WordPress и эмуляцией атак.

## Архитектура решения

В рамках Kubernetes-кластера разворачиваются следующие компоненты:

* **cert-manager** — автоматическое управление TLS-сертификатами (Let’s Encrypt)
* **VictoriaLogs Cluster** — распределённое хранилище логов
* **Victoria Metrics K8s Stack** — сбор метрик (Prometheus-совместимый стек)
* **Log Generators** — генераторы логов (nginx, python-приложения)
* **Ingress Controller (nginx)** — источник access/error логов

Такой стек позволяет не только хранить логи, но и коррелировать их с метриками и событиями безопасности.

## Установка cert-manager

Для работы ingress с TLS используется cert-manager.

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.19.2 \
  --wait \
  --timeout 15m \
  --set crds.enabled=true
```

После установки применяется `ClusterIssuer`, который будет использоваться ingress-ресурсами для автоматического выпуска сертификатов:

```bash
kubectl apply -f cluster-issuer.yaml
```

## Развёртывание VictoriaLogs Cluster

VictoriaLogs устанавливается через официальный Helm-репозиторий VictoriaMetrics.

```bash
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update

kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster \
  -n victorialogs \
  --wait \
  --version 0.0.24 \
  --timeout 15m \
  -f victorialogs-cluster-values.yaml
```

### Почему кластерный режим?

* горизонтальное масштабирование
* отказоустойчивость
* высокая скорость записи логов
* подходит для production-нагрузок

## Генерация логов

Для демонстрации и тестирования используются несколько источников логов.

### NGINX Log Generator
Генерирует HTTP access-логи, близкие к реальным ingress-сценариям.

```bash
kubectl create ns nginx-log-generator
kubectl apply -f nginx-log-generator.yaml
```

### Log Generator
```bash
kubectl create ns flog-log-generator
kubectl apply -f flog-log-generator.yaml
```

## Развёртывание victoria-logs-collector

victoria-logs-collector устанавливается через официальный Helm-репозиторий VictoriaMetrics.

```bash
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update

kubectl create ns victoria-logs-collector
helm upgrade --install vlc vm/victoria-logs-collector \
  -n victoria-logs-collector \
  --wait \
  --version 0.2.2 \
  --timeout 15m \
  -f victoria-logs-collector-values.yaml
```

Открываем http://victorialogs.apatsev.org.ru/select/vmui и смотрим

* всплески 4xx/5xx,
* аномальные паттерны запросов,
* сигнатуры атак в логах ingress и приложения.

## Производительность и преимущества VictoriaLogs

### Ключевые преимущества

1. **Высокая производительность**:
   - Обработка миллионов строк логов в секунду на одной ноде
   - Низкая задержка запросов (<100 мс для большинства операций)
   - Эффективное сжатие данных (до 15x по сравнению с сырыми логами)
   - Быстрый full-text search с задержкой <100 мс
   - Поддержка до 10 миллионов запросов в секунду на одной ноде

2. **Экономия ресурсов**:
   - До 30x меньшее потребление RAM по сравнению с Elasticsearch
   - До 15x меньшее потребление disk space по сравнению с Elasticsearch

3. **Простота эксплуатации**:
   - Единый бинарный файл без внешних зависимостей
   - Простая конфигурация через командную строку или переменные окружения
   - Нативная интеграция с Kubernetes через Helm

4. **Масштабируемость**:
   - Горизонтальное масштабирование в кластерном режиме
   - Линейное увеличение производительности с добавлением нод
   - Поддержка многопоточности для параллельной обработки запросов

### Сравнение с альтернативами

| Функция | VictoriaLogs | Elasticsearch | Grafana Loki |
|---------|--------------|---------------|--------------|
| Простота установки | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Потребление ресурсов | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| Скорость запросов | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Масштабируемость | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Стоимость эксплуатации | ⭐⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐ |

### Бенчмарки производительности

Согласно [официальным бенчмаркам](https://docs.victoriametrics.com/victorialogs/README.md#benchmarks):
- VictoriaLogs показывает в 2-5 раз лучшую производительность по сравнению с Elasticsearch
- В 3-10 раз лучшее сжатие данных
- На 70-90% меньшее потребление памяти по сравнению с Elasticsearch
- Поддержка до 10 миллионов запросов в секунду на одной ноде
- До 1000x ускорение haystack search (поиск редких терминов в большом объёме логов)
- Эффективное использование bloom filters вместо inverted indexes
- Поддержка wide events с сотнями полей

## Практическая ценность VictoriaLogs в Kubernetes

VictoriaLogs в Kubernetes позволяет:

* централизованно хранить логи без Elasticsearch
* обрабатывать миллионы строк в секунду
* быстро выполнять search и filtering
* эффективно работать с security-логами
* коррелировать логи с метриками VictoriaMetrics

В сочетании с реальными сценариями (WordPress + атаки) это делает VictoriaLogs отличной основой для:

* observability,
* troubleshooting,
* security monitoring,
* SOC / SIEM-like use cases.

## Что можно делать с логами в VictoriaLogs

VictoriaLogs предоставляет мощный язык запросов [LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/), который позволяет выполнять сложный анализ логов:

### Поиск и фильтрация
* **Full-text search** - поиск по любому тексту в логах
* **Field-based filtering** - фильтрация по конкретным полям
* **Time-range queries** - анализ логов за определённый период
* **Regex pattern matching** - поиск по регулярным выражениям
* **Phrase search** - поиск точных фраз

### Статистический анализ и агрегация
* **Counting and aggregation** - подсчёт и группировка логов
* **Statistical functions** - вычисление средних, перцентилей и т.д.
* **Time series analysis** - анализ временных рядов логов
* **Correlation analysis** - корреляция логов с метриками

### Примеры запросов LogsQL

```logsql
# Поиск ошибок в логах за последний час
_time:1h error

# Подсчёт запросов по IP-адресам
_time:1h | stats by (ip) count() requests

# Анализ HTTP статусов
_time:1h | stats count() if (status:4*) as client_errors, count() if (status:5*) as server_errors

# Поиск подозрительных паттернов
_time:1h | filter user_agent:~"*bot*|*crawler*" | fields ip, user_agent

# Мониторинг аномальных запросов
_time:1h | stats by (ip) count() requests, count() if (status:4*) errors | filter errors:>10
```

### Мониторинг и алертинг

VictoriaLogs интегрируется с [vmalert](https://docs.victoriametrics.com/victorialogs/vmalert/) для создания алертов на основе логов. vmalert использует статистические API VictoriaLogs:

* [`/select/logsql/stats_query`](https://docs.victoriametrics.com/victorialogs/vmalert/) для создания алертов на основе логов:

```yaml
groups:
  - name: ServiceLog
    type: vlogs
    interval: 5m
    rules:
      - alert: HasErrorLog
        expr: 'env: "prod" AND status:~"error|warn" | stats by (service, kubernetes.pod) count() as errorLog | filter errorLog:>0'
        annotations:
          description: 'Service {{$labels.service}} (pod {{ index $labels "kubernetes.pod" }}) generated {{$labels.errorLog}} error logs in the last 5 minutes'

  - name: ServiceRequest
    type: vlogs
    interval: 5m
    rules:
      - alert: TooManyFailedRequest
        expr: '* | extract "ip=<ip> " | extract "status_code=<code>;" | stats by (ip) count() if (code:~4.*) as failed, count() as total| math failed / total as failed_percentage| filter failed_percentage :> 0.01 | fields ip,failed_percentage'
        annotations:
          description: "Connection from address {{$labels.ip}} has {{$value}}% failed requests in last 5 minutes"

  - name: RequestDuration
    type: vlogs
    interval: 5m
    rules:
      - record: requestDurationQuantile
        expr: '* | stats by (service) quantile(0.5, request_duration_seconds) p50, quantile(0.9, request_duration_seconds) p90, quantile(0.99, request_duration_seconds) p99'
```

#### Правила записи (Recording Rules)

```yaml
groups:
  - name: RequestCount
    type: vlogs
    interval: 5m
    rules:
      - record: nginxRequestCount
        expr: 'env: "test" AND service: "nginx" | stats count(*) as requests'
      - record: prodRequestCount
        expr: 'env: "prod" | stats by (service) count(*) as requests'
```

### Визуализация в Grafana

VictoriaLogs имеет официальный [Grafana datasource plugin](https://docs.victoriametrics.com/victorialogs/victorialogs-datasource/) позволяет:
* Создавать дашборды для мониторинга логов
* Строить графики на основе агрегированных данных логов
* Настраивать алерты прямо из Grafana
* Использовать LogsQL для сложных запросов

### Интеграция с экосистемой observability

* **VictoriaMetrics** - единая платформа для метрик и логов
* **Prometheus** - совместимость с PromQL через VictoriaMetrics
* **OpenTelemetry** - поддержка стандартных протоколов
* **Kubernetes** - нативная интеграция с k8s логами

### Безопасность и compliance

* **Audit logging** - сбор аудит-логов Kubernetes
* **Security monitoring** - обнаружение аномалий и атак
* **Compliance reporting** - отчёты для регуляторных требований
* **Data retention policies** - настройка политик хранения логов

## Практические примеры использования VictoriaLogs

### Мониторинг ошибок приложений

```logsql
# Поиск всех ERROR логов за последние 24 часа
_time:24h | filter level:ERROR | fields _time, service, message

# Анализ производительности API
_time:1h | extract "duration=<duration>" | stats 
  quantile(0.5, duration) p50,
  quantile(0.9, duration) p90,
  quantile(0.99, duration) p99

# Обнаружение подозрительных IP-адресов
_time:1h | stats by (ip) count() requests, count() if (status:4*) errors | 
  filter errors:>100 | fields ip, errors

# Мониторинг трафика ботов
_time:1h | filter user_agent:~"*bot*|*crawler*" | stats by (user_agent) count() requests

# Поиск SQL-инъекций в логах
_time:1h | filter message:~"*select*|*insert*|*update*|*delete*" | fields _time, ip, message

# Анализ паттернов доступа
_time:7d | stats by (ip) count() requests, count() if (status:4*) errors, count() if (status:5*) server_errors

# Мониторинг аномальных паттернов запросов
_time:1h | stats by (endpoint) count() requests, count() if (status:4*) client_errors
```

### Алертинг с vmalert

```yaml
groups:
  - name: ApplicationMonitoring
    type: vlogs
    interval: 5m
    rules:
      - alert: HighErrorRate
        expr: '_time:5m | stats count() if (level:ERROR) errors, count() total | math errors / total as error_rate | filter error_rate:>0.05'
        annotations:
          description: 'Error rate {{$value}} exceeds threshold'

  - name: SecurityMonitoring
    type: vlogs
    interval: 1m
    rules:
      - alert: SuspiciousActivity
        expr: '_time:1m | stats by (ip) count() requests | filter requests:>1000'
        annotations:
          description: 'IP {{$labels.ip}} made {{$value}} requests in the last minute'

  - name: PerformanceMonitoring
    type: vlogs
    interval: 5m
    rules:
      - record: apiResponseTime
        expr: '_time:5m | stats by (service) quantile(0.95, response_time) p95'
```

### Преимущества VictoriaLogs

* **Высокая производительность** - до 10x быстрее чем Elasticsearch на production-нагрузках
* **Низкое потребление ресурсов** - до 10x меньше RAM и disk space
* **Простота установки** - один Helm chart для всего кластера
* **LogsQL** - простой и мощный язык запросов
* **Нативная интеграция с Kubernetes** - автоматическое парсинг логов контейнеров
* **Горизонтальное масштабирование** - легко добавлять ноды
* **Production-ready** - подходит для enterprise-нагрузок

### Интеграция с Kubernetes

VictoriaLogs автоматически:
* Собирает логи всех контейнеров
* Индексирует все поля логов
* Поддерживает multitenancy
* Интегрируется с cert-manager для автоматического TLS
* Работает с существующими log collectors (FluentBit, Filebeat, Vector, etc.)
* Предоставляет мощный Web UI для анализа логов

## Мониторинг: Victoria Metrics K8s Stack

Для мониторинга инфраструктуры разворачивается Victoria Metrics K8s Stack.

```bash
kubectl create ns vmks
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
helm upgrade --install vmks vm/victoria-metrics-k8s-stack \
  -n vmks \
  --wait \
  --version 0.66.1 \
  --timeout 15m \
  -f vmks-values.yaml
```

Открываем https://grafana.apatsev.org.ru/ и смотрим нагрузку на систему

Получение пароля grafana для admin юзера
```shell
kubectl get secret vmks-grafana -n vmks -o jsonpath='{.data.admin-password}' | base64 --decode; echo
```

## Заключение

VictoriaLogs — зрелое и production-ready решение для логирования в Kubernetes. Простота установки через Helm, высокая производительность и нативная интеграция с экосистемой VictoriaMetrics делают его отличной альтернативой тяжёлым ELK-стекам, особенно в cloud-native средах.
