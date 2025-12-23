# Overview: VictoriaLogs in Kubernetes

## Введение

**VictoriaLogs** — это высокопроизводительное хранилище логов от команды VictoriaMetrics, оптимизированное под большие объёмы данных, низкое потребление ресурсов и простоту эксплуатации. В Kubernetes VictoriaLogs органично вписывается в экосистему observability и может использоваться как централизованное лог-хранилище для приложений, ingress-контроллеров и security-событий.

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
  --version 0.0.22 \
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

```bash
kubectl apply -f nginx-log-generator.yaml
```

Генерирует HTTP access-логи, близкие к реальным ingress-сценариям.

### Python Log Generator

Сборка и публикация Docker-образа:

```bash
docker build -t antonpatsev/log-generator:2 .
docker push antonpatsev/log-generator:2
kubectl apply -f python-log-generator.yaml
```

Позволяет эмулировать application-level логи (INFO, WARN, ERROR).

Открываем https://victorialogs.apatsev.org.ru/select/vmui и смотрим

* всплески 4xx/5xx,
* аномальные паттерны запросов,
* сигнатуры атак в логах ingress и приложения.

## Практическая ценность VictoriaLogs

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

VictoriaLogs интегрируется с [vmalert](https://docs.victoriametrics.com/victorialogs/vmalert/) для создания алертов на основе логов:

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
```

### Визуализация в Grafana

VictoriaLogs имеет официальный [Grafana datasource plugin](https://docs.victoriametrics.com/victorialogs/victorialogs-datasource/), который позволяет:
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

## Мониторинг: Victoria Metrics K8s Stack

Для мониторинга инфраструктуры разворачивается Victoria Metrics K8s Stack.

```bash
kubectl create ns vmks
helm upgrade --install vmks vm/victoria-metrics-k8s-stack \
  -n vmks \
  --wait \
  --version 0.66.0 \
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

TODO
https://github.com/mingrammer/flog
https://github.com/psemiletov/logfilegen
