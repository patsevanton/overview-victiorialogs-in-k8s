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
timestamp missing http.status_code: 401 count: 1
timestamp missing http.status_code: 404 count: 1
timestamp missing http.status_code: 500 count: 1
timestamp missing http.status_code: 200 count: 1
timestamp missing http.status_code: 403 count: 2
```

**Счетчики по статусам. По всем логам за 5 последние 5 минут**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.status_code) count() as requests | sort by (requests desc)
```

Вывод
```
timestamp missing requests: 10 http.status_code: 401
timestamp missing requests: 10 http.status_code: 403
timestamp missing requests: 9 http.status_code: 200
timestamp missing requests: 8 http.status_code: 500
timestamp missing requests: 6 http.status_code: 404
```

**Топ медленных запросов:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | limit 10
```

вывод
```
timestamp missing max_time: 1.9978073 http.url: api.example.com/api/v1/users?RequestId=a1b2c3d4-e5f6-7890-abcd-ef1234567890
timestamp missing max_time: 1.9970258 http.url: api.example.com/api/v1/products?RequestId=1ab2c345-d6e7-4890-b1c2-d3e4f5a6b7c8
timestamp missing max_time: 1.9878687 http.url: api.example.com/api/v1/users?RequestId=123e4567-e89b-12d3-a456-426614174000
timestamp missing max_time: 1.9555196 http.url: api.example.com/api/v1/users?RequestId=f47ac10b-58cc-4372-a567-0e02b2c3d479
timestamp missing max_time: 1.9316189 http.url: api.example.com/api/v1/products?RequestId=0fc0f571-d3c4-4e75-8a6f-3f9f137edbb8
```

**Ошибки по IP-адресам:**
```
kubernetes.pod_namespace: "nginx-log-generator" | http.status_code:>=400 | stats by (nginx.remote_addr) count() as errors
```
Вывод
```
timestamp missing nginx.remote_addr: 10.0.0.3 errors: 61
timestamp missing nginx.remote_addr: 10.0.0.2 errors: 80
timestamp missing nginx.remote_addr: 10.0.0.1 errors: 103
```

**Доля ошибок:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats count() as total, count() if (http.status_code:>=400) as errors | math errors / total * 100 as error_rate
```
Вывод
```
timestamp missing total: 299 errors: 247 error_rate: 82.6086956521739
```

**Трафик по URL:**
```
kubernetes.pod_namespace: "nginx-log-generator" | stats by (http.url) sum(http.bytes_sent) as total_bytes | sort by (total_bytes desc) | limit 5
```

вывод
```
timestamp missing total_bytes: 33117 http.url: api.example.com/api/v1/users?RequestId=123e4567-e89b-12d3-a456-426614174000
timestamp missing total_bytes: 31980 http.url: api.example.com/api/v1/users?RequestId=a1b2c3d4-e5f6-7890-abcd-ef1234567890
timestamp missing total_bytes: 31625 http.url: api.example.com/api/v1/users?RequestId=f47ac10b-58cc-4372-a567-0e02b2c3d479
timestamp missing total_bytes: 25118 http.url: api.example.com/api/v1/products?RequestId=1ab2c345-d6e7-4890-b1c2-d3e4f5a6b7c8
timestamp missing total_bytes: 18680 http.url: api.example.com/api/v1/products?RequestId=0fc0f571-d3c4-4e75-8a6f-3f9f137edbb8
```

## LogsQL: язык запросов VictoriaLogs

**LogsQL** — это потоковый (pipeline) язык запросов для работы с логами в VictoriaLogs.
Он сочетает полнотекстовый поиск, фильтрацию, извлечение полей и агрегации в одном запросе.

Запрос состоит из **последовательности стадий**, разделённых оператором `|`.

### Общая структура запроса

```
<filtering> | <parsing/extract> | <transform> | <aggregation> | <post-filter>
```

### Фильтр по полям

```
http.status_code:200
http.status_code:>=400
http.method:GET
kubernetes.pod_namespace:"default"
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
_time:10m "error" kubernetes.pod_name:"nginx-log-generator"
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
| fields _time, level, _msg, kubernetes.pod_name
```

### `sort`

Сортировка результатов:

```
| sort by (_time desc)
| sort by (requests desc)
```

### `limit`

Ограничение количества строк:

```
| limit 10
| limit 5 by (errors desc)
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
| unpack_json
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
_time:5m | stats by (http.url) sum(http.bytes_sent) as bytes | sort by (bytes desc) | limit 10
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
limit 10
```

### Медленные запросы

```
_time:5m |
stats by (http.url) max(request_time) as max_time |
sort by (max_time desc) |
limit 5
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
| Ограничение       | `\| limit 10`                  |
| Вычисление        | `\| math a / b * 100`          |
