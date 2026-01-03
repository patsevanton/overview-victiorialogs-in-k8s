# VictoriaLogs в Kubernetes: от установки до практического применения

Руководство по развёртыванию и использованию VictoriaLogs в Kubernetes. Документ фокусируется на практических шагах: установка через Helm, интеграция с cert-manager и Ingress, генерация логов, примеры запросов в LogsQL и интеграция с экосистемой наблюдаемости.


## Оглавление

- [VictoriaLogs в Kubernetes: от установки до практического применения](#victorialogs-в-kubernetes-от-установки-до-практического-применения)
  - [Оглавление](#оглавление)
  - [Введение](#введение)
  - [Ключевые концепции и преимущества](#ключевые-концепции-и-преимущества)
  - [Архитектура решения](#архитектура-решения)
  - [Подготовка к установке](#подготовка-к-установке)
  - [Установка компонентов (практика)](#установка-компонентов-практика)
    - [1) cert-manager](#1-cert-manager)
    - [2) VictoriaLogs Cluster](#2-victorialogs-cluster)
    - [3) collector (victoria-logs-collector)](#3-collector-victoria-logs-collector)
    - [4) VM K8s Stack (метрики, Grafana)](#4-vm-k8s-stack-метрики-grafana)
  - [Генерация тестовых логов](#генерация-тестовых-логов)
  - [Быстрый вход в LogsQL (cheatsheet)](#быстрый-вход-в-logsql-cheatsheet)
  - [Примеры запросов](#примеры-запросов)
  - [Интеграция: Grafana, vmalert, OpenTelemetry](#интеграция-grafana-vmalert-opentelemetry)
  - [Безопасность, хранение и retention](#безопасность-хранение-и-retention)
  - [Полезные ссылки](#полезные-ссылки)
  - [Заключение](#заключение)


## Введение

**VictoriaLogs** — высокопроизводительное хранилище логов от команды VictoriaMetrics. Оптимизировано для больших объёмов логов, поддерживает эффективное хранение "wide events" (множество полей в записи), быстрые полнотекстовые поиски и масштабирование.

В Kubernetes VictoriaLogs обычно используется совместно с: cert-manager, Ingress (NGINX), сборщиками логов (Vector, Fluentd/Fluent Bit, Filebeat, Promtail), системами метрик (VictoriaMetrics / Prometheus) и визуализации в Grafana.

Цель этого документа — дать понятную, проверенную на практике инструкцию для развёртывания стека и базовой работы с LogsQL.


## Ключевые концепции и преимущества

- Быстрое полнотекстовое и аналитическое чтение логов благодаря оптимизациям (bloom filters и пр.).
- Низкие требования к ресурсам: экономия RAM и диска по сравнению с традиционными ELK-стеками.
- Поддержка кластерного режима: vlinsert / vlstorage / vlselect.
- LogsQL — удобный pipeline-язык запросов для фильтрации, извлечения и агрегаций.

Преимущества в сравнении с альтернативами (кратко):

| Функция            | VictoriaLogs | Elasticsearch | Grafana Loki |
|--|--|--|--|
| Простота установки | ⭐⭐⭐⭐⭐       | ⭐⭐           | ⭐⭐⭐         |
| Потребление ресурсов | ⭐⭐⭐⭐⭐    | ⭐            | ⭐⭐⭐         |
| Скорость запросов  | ⭐⭐⭐⭐⭐       | ⭐⭐⭐          | ⭐⭐          |
| Масштабируемость   | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐         | ⭐⭐⭐         |
| Стоимость эксплуатации | ⭐⭐⭐⭐⭐  | ⭐            | ⭐⭐⭐⭐        |

> Примечание: конкретные цифры зависят от нагрузки и конфигурации — используйте бенчмарки и тесты на ваших данных.


## Архитектура решения

В Kubernetes-кластере рекомендуется разворачивать следующие компоненты:

- cert-manager: автоматизация выпуска TLS-сертификатов (Let’s Encrypt);
- VictoriaLogs Cluster: vlinsert (ingest), vlstorage (хранилище), vlselect (query);
- victoria-logs-collector / Vector / Fluent Bit: сбор и форвард логов в VictoriaLogs;
- Victoria Metrics K8s Stack (vmks) — сбор метрик и Grafana;
- Ingress Controller (NGINX) — источник access/error логов для приложений;
- Optionally: vlagent для репликации/буферизации.

Архитектура даёт возможность: корректно масштабировать ingestion и storage отдельно, интегрировать метрики и логи и строить оповещения по логам.

## Подготовка к установке

1. Убедитесь, что у вас есть доступ к Kubernetes-кластеру (kubectl настроен).
2. Доступ к Helm 3.
3. В кластере должно быть достаточно ресурсов для выбранной конфигурации (особенно для vlstorage).


## Установка компонентов (практика)

Следующие команды — примерные. Перед применением проверьте версии чарта и значения в своих value-файлах.

### 1) cert-manager

Установите cert-manager для автоматизации TLS:

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

После установки подключите ClusterIssuer (пример файла — [`cluster-issuer.yaml`](cluster-issuer.yaml:1)).

```bash
kubectl apply -f cluster-issuer.yaml
```

> Если вы не используете Let’s Encrypt, замените настройки ClusterIssuer на внутренний CA или нужный вам провайдер.

### 2) VictoriaLogs Cluster

Установка через официальный Helm-чарт (пример):

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

Удаление:

```bash
helm uninstall -n victoria-logs-cluster victoria-logs-cluster
```

> В production-окружении настраивайте TLS/mTLS и авторизацию между компонентами кластера (см. раздел Security в официальной документации).

### 3) collector (victoria-logs-collector)

Чарт для развёртывания collector/ingest-агента:

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


### 4) VM K8s Stack (метрики, Grafana)

Пример установки victoria-metrics-k8s-stack c Grafana:

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

 Можно анализировать логи через explore Grafana.
 Для получения пароля admin от Grafana необходимо:

```bash
# Откройте http://grafana.apatsev.org.ru/
kubectl get secret vmks-grafana -n vmks -o jsonpath='{.data.admin-password}' | base64 --decode; echo
```

Либо можете анализировать логи через VMUI

Интерфейс VMUI (http://victorialogs.apatsev.org.ru/select/vmui)


## Генерация тестовых логов

Для нагрузочного тестирования и примеров показаны генераторы логов. Примеры ресурсов для Kubernetes:

- NGINX log generator (pod манифест) — пример конфигурации размещён в YAML:

```yaml
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
    image: ghcr.io/patsevanton/generator-log-nginx:1.6.4
    env:
    - name: RATE
      value: "1"
    - name: IP_ADDRESSES
      value: "10.0.0.1,10.0.0.2,10.0.0.3"
    - name: HTTP_METHODS
      value: "GET,POST"
    - name: PATHS
      value: "/api/v1/products?RequestId=0fc0f571-d3c4-4e75-8a6f-3f9f137edbb8,/api/v1/products?RequestId=1ab2c345-d6e7-4890-b1c2-d3e4f5a6b7c8,/api/v1/users?RequestId=a1b2c3d4-e5f6-7890-abcd-ef1234567890,/api/v1/users?RequestId=123e4567-e89b-12d3-a456-426614174000,/api/v1/users?RequestId=f47ac10b-58cc-4372-a567-0e02b2c3d479"
    - name: STATUS_CODES
      value: "200,401,403,404,500"
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

Пример команд управления генератором:

```bash
kubectl create ns nginx-log-generator
kubectl apply -f nginx-log-generator.yaml
# проверить логи, затем
kubectl delete -f nginx-log-generator.yaml
```

Для других генераторов (flog, python и т.д.) используйте аналогичный паттерн (namespace → apply → delete).


## Быстрый вход в LogsQL (cheatsheet)

LogsQL — pipeline-язык. Короткий набор базовых операций:

- Фильтр по времени: `_time:5m`, `_time:1h`, `_time:24h`
- Поиск слова: `"error"` или `"/api/v1/login"`
- Фильтр по полю: `http.status_code:>=400`, `kubernetes.pod_namespace:"nginx-log-generator"`
- Аггрегация: `| stats by (http.status_code) count() as requests`
- Извлечение: `| extract "duration=(\d+)"`
- Unpack JSON: `| unpack_json`
- Сортировка: `| sort by (requests desc)`
- Лимит: `| limit 10`
- `stats` — агрегации и функции (count, sum, avg, min, max, quantile, row_any и пр.).
- `extract` / `extract_regexp` — извлечение по регулярным выражениям.
- `unpack_json` / `unpack_logfmt` — развёртывание структурированных полей.
- `fields` — выбор столбцов для вывода.
- `sort`, `limit`, `filter`, `math` — постобработка.


Краткая структура запроса:

```
<filter> | <parsing/extract> | <transform> | <aggregation> | <post-filter>
```


## Примеры запросов

1) Счётчики по статусам для namespace nginx-log-generator:

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.status_code) count() as requests | sort by (requests desc)
```

2) Топ медленных URL по времени ответа:

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | limit 10
```

3) IP с наибольшим количеством ошибок:

```
kubernetes.pod_namespace:"nginx-log-generator" | http.status_code:>=400 | stats by (nginx.remote_addr) count() as errors | sort by (errors desc) | limit 10
```

4) Доля ошибок (percent):

```
kubernetes.pod_namespace:"nginx-log-generator" |
  stats count() as total, count() if (http.status_code:>=400) as errors |
  math errors / total * 100 as error_rate
```

5) Поиск подозрительных попыток входа (анализ аномалий):

```
_time:1h "failed login" | stats by (user, ip) count() as attempts | filter attempts:>20
```


## Интеграция: Grafana, vmalert, OpenTelemetry

- Grafana: используйте официальный плагин VictoriaLogs Datasource для дашбордов и визуализации LogsQL-запросов.
- vmalert: позволяет строить алерты по логам (через `/select/logsql/stats_query` API). Пример правила:

```yaml
groups:
  - name: ServiceLog
    type: vlogs
    interval: 5m
    rules:
      - alert: HasErrorLog
        expr: 'env: "prod" AND status:~"error|warn" | stats by (service, kubernetes.pod) count() as errorLog | filter errorLog:>0'
        annotations:
          description: 'Service {{$labels.service}} generated {{$labels.errorLog}} error logs in the last 5 minutes'
```

- OpenTelemetry: VictoriaLogs совместим с OpenTelemetry ingestion (через vlinsert/collector).


## Безопасность, хранение и retention

- Настройте TLS/mTLS для внутренних коммуникаций в кластерной конфигурации.
- Используйте авторизацию (vmauth / реверс-прокси) для защиты HTTP API.
- Политики хранения: per-day partitions, snapshot/restore через internal endpoints; возможен retention по месту на диске.


## Полезные ссылки

- Официальная документация VictoriaLogs: https://docs.victoriametrics.com/victorialogs/
- LogsQL: https://docs.victoriametrics.com/victorialogs/logsql/
- vmalert (alerting): https://docs.victoriametrics.com/victoriametrics/vmalert/


## Заключение

VictoriaLogs — зрелое решение для production-логирования в Kubernetes. Оно даёт высокую производительность при небольших ресурсных затратах, обеспечивает удобный язык запросов и интеграцию с экосистемой (Grafana, vmalert, OpenTelemetry). Рекомендуется протестировать чарт на реальных объёмах данных перед переносом в production и настроить TLS/авторизацию для защиты данных.
