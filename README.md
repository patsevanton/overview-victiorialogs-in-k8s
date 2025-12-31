# VictoriaLogs в Kubernetes: от установки до практического применения

## Введение

**VictoriaLogs** — это высокопроизводительное хранилище логов, разработанное командой VictoriaMetrics. Оно оптимизировано для работы с большими объёмами данных, отличается низким потреблением ресурсов и простотой эксплуатации. В экосистеме Kubernetes VictoriaLogs органично интегрируется в инфраструктуру observability, выступая в качестве централизованного хранилища логов для приложений, ingress-контроллеров и событий безопасности.

В этой статье рассматривается:

- архитектура VictoriaLogs в Kubernetes,
- установка через Helm,
- интеграция с cert-manager и ingress,
- генерация логов и метрик,
- пример практического сценария с WordPress и эмуляцией атак.

## Архитектура решения

В Kubernetes-кластере разворачиваются следующие компоненты:

- **cert-manager** — автоматическое управление TLS-сертификатами (Let’s Encrypt);
- **VictoriaLogs Cluster** — распределённое хранилище логов;
- **Victoria Metrics K8s Stack** — сбор метрик (Prometheus-совместимый стек);
- **Log Generators** — генераторы логов (nginx, python-приложения);
- **Ingress Controller (nginx)** — источник access/error логов.

Данный стек позволяет не только хранить логи, но и коррелировать их с метриками и событиями безопасности.

## Установка и настройка компонентов

### 1. Установка cert-manager

Для работы ingress с TLS используется cert-manager.

```bash
helm install \
  cert-manager oci://quay.io/jetstack/charts/cert-manager \
  --version v1.19.2 \
  --namespace cert-manager \
  --create-namespace \
  --set crds.enabled=true \
  --wait \
  --timeout 15m
```

После установки применяется `ClusterIssuer` для автоматического выпуска сертификатов:

```bash
kubectl apply -f cluster-issuer.yaml
```

### 2. Развёртывание VictoriaLogs Cluster

VictoriaLogs устанавливается через официальный Helm-репозиторий VictoriaMetrics.

```bash
helm upgrade --install victoria-logs-cluster \
  oci://ghcr.io/victoriametrics/helm-charts/victoria-logs-cluster \
  --namespace victoria-logs-cluster \
  --create-namespace \
  --wait \
  --version 0.0.24 \
  --timeout 15m \
  -f victorialogs-cluster-values.yaml
```

**Преимущества кластерного режима:**

- горизонтальное масштабирование;
- отказоустойчивость;
- высокая скорость записи логов;
- подходит для production-нагрузок.

### 3. Развёртывание victoria-logs-collector

```bash
helm upgrade --install victoria-logs-collector \
  oci://ghcr.io/victoriametrics/helm-charts/victoria-logs-collector \
  --namespace victoria-logs-collector \
  --create-namespace \
  --wait \
  --version 0.2.4 \
  --timeout 15m \
  -f victoria-logs-collector-values.yaml
```

### 5. Мониторинг: Victoria Metrics K8s Stack

```bash
helm upgrade --install vmks \
  oci://ghcr.io/victoriametrics/helm-charts/victoria-metrics-k8s-stack \
  --namespace vmks \
  --create-namespace \
  --wait \
  --version 0.66.1 \
  --timeout 15m \
  -f vmks-values.yaml
```

**Доступ к Grafana:**
- Открыть http://grafana.apatsev.org.ru/
- Получить пароль администратора:

```bash
kubectl get secret vmks-grafana -n vmks -o jsonpath='{.data.admin-password}' | base64 --decode; echo
```

## Анализ логов через VMUI

Интерфейс VMUI (http://victorialogs.apatsev.org.ru/select/vmui) позволяет анализировать:

- всплески 4xx/5xx ошибок;
- аномальные паттерны запросов;
- сигнатуры атак в логах ingress и приложений.

## Производительность и преимущества VictoriaLogs

### Ключевые преимущества

1. **Высокая производительность:**
   - Обработка миллионов строк логов в секунду на одной ноде;
   - Низкая задержка запросов (<100 мс);
   - Эффективное сжатие данных (до 15x);
   - Быстрый full-text search (<100 мс);
   - Поддержка до 10 миллионов запросов в секунду на одной ноде.

2. **Экономия ресурсов:**
   - До 30x меньше RAM по сравнению с Elasticsearch;
   - До 15x меньше disk space по сравнению с Elasticsearch.

3. **Простота эксплуатации:**
   - Единый бинарный файл без внешних зависимостей;
   - Простая конфигурация;
   - Нативная интеграция с Kubernetes через Helm.

4. **Масштабируемость:**
   - Горизонтальное масштабирование в кластерном режиме;
   - Линейный рост производительности;
   - Поддержка многопоточности.

### Сравнение с альтернативами

| Функция            | VictoriaLogs | Elasticsearch | Grafana Loki |
|--|--|--|--|
| Простота установки | ⭐⭐⭐⭐⭐       | ⭐⭐           | ⭐⭐⭐         |
| Потребление ресурсов | ⭐⭐⭐⭐⭐    | ⭐            | ⭐⭐⭐         |
| Скорость запросов  | ⭐⭐⭐⭐⭐       | ⭐⭐⭐          | ⭐⭐          |
| Масштабируемость   | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐         | ⭐⭐⭐         |
| Стоимость эксплуатации | ⭐⭐⭐⭐⭐  | ⭐            | ⭐⭐⭐⭐        |

### Официальные бенчмарки

Согласно [официальным бенчмаркам](https://docs.victoriametrics.com/victorialogs/README.md#benchmarks):
- Производительность в 2–5 раз выше, чем у Elasticsearch;
- Сжатие данных в 3–10 раз эффективнее;
- Потребление памяти на 70–90% меньше;
- Поддержка до 10 миллионов запросов в секунду на одной ноде;
- До 1000x ускорение haystack search;
- Эффективное использование bloom filters вместо inverted indexes;
- Поддержка wide events с сотнями полей.

## Практическое применение VictoriaLogs


### 4. Генерация логов

Для тестирования используются несколько источников логов.

**NGINX Log Generator:**
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-log-generator
  namespace: nginx-log-generator
  labels:
    app: nginx-log-generator
spec:
  containers:
  - name: nginx-log-generator
    image: ghcr.io/patsevanton/generator-log-nginx:1.6.3
    env:
    - name: RATE
      value: "1"
    - name: IP_ADDRESSES
      value: "10.0.0.1,10.0.0.2"
    - name: HTTP_METHODS
      value: "GET,POST"
    - name: PATHS
      value: "/api/v1/products?RequestId=0fc0f571-d3c4-4e75-8a6f-3f9f137edbb8,/api/v1/products?RequestId=1ab2c345-d6e7-4890-b1c2-d3e4f5a6b7c8,/api/v1/users?RequestId=a1b2c3d4-e5f6-7890-abcd-ef1234567890,/api/v1/users?RequestId=123e4567-e89b-12d3-a456-426614174000,/api/v1/users?RequestId=f47ac10b-58cc-4372-a567-0e02b2c3d479"
    - name: STATUS_CODES
      value: "200,401"
    - name: HOSTS
      value: "api.example.com"
    resources:
      requests:
        memory: "64Mi"
        cpu: "100m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```


```bash
kubectl create ns nginx-log-generator
kubectl apply -f nginx-log-generator.yaml
```

**Log Generator:**
```bash
kubectl create ns flog-log-generator
kubectl apply -f flog-log-generator.yaml
```

### Анализ логов с использованием LogsQL

VictoriaLogs предоставляет мощный язык запросов [LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/). Примеры запросов:


## 1. Фильтрация логов

### Фильтр по времени

```
* # время указывается в UI
```

```
_time:5m      # последние 5 минут
_time:1h      # последний час
_time:24h     # последние сутки
```

**График status_code по ручке /api/v1/products. По namespace nginx-log-generator**
```
kubernetes.pod_namespace: "nginx-log-generator" | "/api/v1/products" | stats by (http.status_code) count() as count 
```

Вывод
```
timestamp missing http.status_code: 401 count: 5
timestamp missing http.status_code: 200 count: 8
```

**Счетчики по статусам. По всем логам за 5 последние 5 минут**
```
_time:5m | stats by (http.status_code) count() as requests | sort by (requests desc)
```

Вывод
```
timestamp missing requests: 87
timestamp missing requests: 77 http.status_code: 200
timestamp missing requests: 35 http.status_code: 401
timestamp missing requests: 1 http.status_code: 302
timestamp missing requests: 1 http.status_code: 400
```

**Топ медленных запросов:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | first 10
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time) | first 10
```

**Ошибки по IP-адресам:**
```
kubernetes.pod_namespace: "nginx-log-generator" | http.status_code:>=400 | stats by (nginx.remote_addr) count() as errors | first 10 by (errors desc)
```
Вывод
```
timestamp missing errors: 79 nginx.remote_addr: 10.0.0.2
timestamp missing errors: 70 nginx.remote_addr: 10.0.0.1
```

**Доля ошибок:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats count() as total, count() if (http.status_code:>=400) as errors | math errors / total * 100 as error_rate
```
Вывод
```
timestamp missing total: 2726errors: 1403error_rate: 51.46735143066764
```

**Трафик по URL:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.url) sum(http.bytes_sent) as total_bytes | sort by (total_bytes desc) | first 5
```

## LogsQL: язык запросов VictoriaLogs

**LogsQL** — это потоковый (pipeline) язык запросов для работы с логами в VictoriaLogs.
Он сочетает полнотекстовый поиск, фильтрацию, извлечение полей и агрегации в одном запросе.

Запрос состоит из **последовательности стадий**, разделённых оператором `|`.

### Общая структура запроса

```
<filtering> | <parsing/extract> | <transform> | <aggregation> | <post-filter>
```

Пример:

```
kubernetes.pod_namespace: "nginx-log-generator" | kubernetes.namespace:"nginx" | extract "status=(\d+)" | stats by (status) count()
```


### Фильтр по полям

```
status:200
status_toggle:>=400
method:GET
kubernetes.namespace:"default"
```

Поддерживаются операторы сравнения:

* `=`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

### Поиск по строке (full-text search)

```
"error"
"/api/v1/login"
"timeout exceeded"
```

Можно комбинировать:

```
_time:10m "error" kubernetes.pod:"nginx"
```

## 2. Операторы пайплайна

### `filter`

Дополнительная фильтрация после агрегаций или вычислений:

```
| filter status:>=500
```

### `fields`

Выбор нужных полей (аналог SELECT):

```
| fields _time, level, message, kubernetes.pod
```

### `sort`

Сортировка результатов:

```
| sort by (_time desc)
| sort by (requests desc)
```

### `first`

Ограничение количества строк:

```
| first 10
| first 5 by (errors desc)
```

## 3. Извлечение данных

### `extract` (regex)

Извлечение значений из текста лога:

```
| extract "duration=(\d+)"
```

С именованными группами:

```
| extract "status=(?<status>\d+)"
```

### `json`

Если лог в JSON-формате:

```
| json
```

После этого поля доступны напрямую:

```
| filter level:"ERROR"
```

## 4. Агрегации и аналитика

### `stats`

Основной оператор агрегации:

```
| stats count()
```

Агрегация по полям:

```
| stats by (status) count() as requests
```

Часто используемые функции:

* `count()`
* `sum(field)`
* `avg(field)`
* `min(field)`
* `max(field)`
* `quantile(0.95, field)`

### Примеры агрегаций

**Количество запросов по статусам:**

```
_time:5m | stats by (http.status_code) count() as requests
```

**Топ URL по трафику:**

```
_time:5m | stats by (http.url) sum(http.bytes_sent) as bytes | sort by (bytes desc) | first 10
```

**P95 latency:**

```
_time:10m | stats quantile(0.95, request_time) as p95
```

## 5. Вычисления

### `math`

Позволяет вычислять новые поля:

```
| math errors / total * 100 as error_rate
```

Пример расчёта процента ошибок:

```
kubernetes.pod_namespace: "nginx-log-generator" |
stats
  count() as total,
  count() if (status:>=400) as errors |
math errors / total * 100 as error_rate
```

## 6. Условия в агрегациях

### `if` внутри `stats`

```
| stats count() if (level:"ERROR") as error_count
```

Пример:

```
_time:5m | stats
  count() as total,
  count() if (status:5*) as server_errors
```

## 7. Практические паттерны

### Топ IP с ошибками

```
_time:10m status:>=400 |
stats by (remote_addr) count() as errors |
sort by (errors desc) |
first 10
```

### Медленные запросы

```
_time:5m |
stats by (http.url) max(request_time) as max_time |
sort by (max_time desc) |
first 5
```

### Поиск аномалий

```
_time:1h "failed login" |
stats by (user, ip) count() as attempts |
filter attempts:>20
```

## 8. Использование LogsQL в Grafana

LogsQL полностью поддерживается в **VictoriaLogs datasource для Grafana**:

* построение time-series графиков;
* таблицы с агрегациями;
* алерты на основе логов;
* единый язык запросов для VMUI и Grafana.



## Краткий cheatsheet LogsQL

| Операция          | Пример                         |
| -- |  |
| Фильтр по времени | `_time:5m`                     |
| Поиск строки      | `"error"`                      |
| Фильтр поля       | `status:>=500`                 |
| JSON              | `\| json`                      |
| Regex extract     | `\| extract "id=(\d+)"`        |
| Агрегация         | `\| stats by (status) count()` |
| Сортировка        | `\| sort by (count desc)`      |
| Ограничение       | `\| first 10`                  |
| Вычисление        | `\| math a / b * 100`          |


### Мониторинг и алертинг

Интеграция с [vmalert](https://docs.victoriametrics.com/victorialogs/vmalert/) позволяет создавать алерты на основе логов:

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

Официальный [Grafana datasource plugin](https://docs.victoriametrics.com/victorialogs/victorialogs-datasource/) позволяет:
- создавать дашборды для мониторинга логов;
- строить графики на основе агрегированных данных;
- настраивать алерты прямо из Grafana;
- использовать LogsQL для сложных запросов.

### Интеграция с экосистемой observability

- **VictoriaMetrics** — единая платформа для метрик и логов;
- **Prometheus** — совместимость с PromQL через VictoriaMetrics;
- **OpenTelemetry** — поддержка стандартных протоколов;
- **Kubernetes** — нативная интеграция с логами k8s.

### Безопасность и compliance

- **Audit logging** — сбор аудит-логов Kubernetes;
- **Security monitoring** — обнаружение аномалий и атак;
- **Compliance reporting** — отчёты для регуляторных требований;
- **Data retention policies** — настройка политик хранения логов.

## Практические примеры использования

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
```

## Заключение

VictoriaLogs — это зрелое и production-ready решение для логирования в Kubernetes. Простота установки через Helm, высокая производительность и нативная интеграция с экосистемой VictoriaMetrics делают его отличной альтернативой ресурсоёмким ELK-стекам, особенно в cloud-native средах.
