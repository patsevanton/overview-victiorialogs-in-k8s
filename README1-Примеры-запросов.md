## 1. Фильтрация логов и временные фильтры

В LogsQL время обычно задаётся короткой формой `_time:<duration>` (например, `5m`, `1h`, `24h`). UI может подставлять временной фильтр автоматически.

Примеры:

```
*                 # время указывается в UI
```

```
_time:5m      # последние 5 минут
_time:1h      # последний час
_time:24h     # последние сутки
```



## 2. Быстрые примеры (nginx-log-generator)

1) Счётчики по статусам для namespace `nginx-log-generator` (за последние 5 минут):

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.status_code) count() as requests | sort by (requests desc)
```

2) Топ медленных URL по времени ответа:

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | limit 10
```

3) IP с наибольшим количеством ошибок (>=400):

```
kubernetes.pod_namespace:"nginx-log-generator" | http.status_code:>=400 | stats by (nginx.remote_addr) count() as errors | sort by (errors desc) | limit 10
```

4) Доля ошибок (процент):

```
kubernetes.pod_namespace:"nginx-log-generator" |
  stats count() as total, count() if (http.status_code:>=400) as errors |
  math errors / total * 100 as error_rate
```

5) Поиск подозрительных попыток входа (анализ аномалий):

```
_time:1h "failed login" | stats by (user, ip) count() as attempts | filter attempts:>20
```



## 3. Примеры дашбордов / графиков

- График распределения `status_code` по ручке `/api/v1/products` для `namespace nginx-log-generator`:

```
kubernetes.pod_namespace: "nginx-log-generator" | "/api/v1/products" | stats by (http.status_code) count() as count
```

- Топ медленных запросов (пример вывода):

```
_time:5m | kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | limit 10
```

Пример строки вывода:

```
timestamp missing max_time: 1.9978073 http.url: api.example.com/api/v1/users?RequestId=a1b2c3...
```

- Ошибки по IP-адресам (пример вывода):

```
timestamp missing nginx.remote_addr: 10.0.0.1 errors: 103
```



## 4. LogsQL — язык запросов VictoriaLogs (кратко)

LogsQL — потоковый (pipeline) язык запросов. Запрос состоит из последовательности стадий, разделённых `|`.

Общая структура:

```
<filtering> | <parsing/extract> | <transform> | <aggregation> | <post-filter>
```

### Примеры фильтров по полям

```
http.status_code:200
http.status_code:>=400
http.method:GET
kubernetes.pod_namespace:"default"
```

Поддерживаемые операторы сравнения: `=`, `!=`, `>`, `<`, `>=`, `<=`.

### Полнотекстовый поиск (full-text)

```
"error"
"/api/v1/login"
"timeout exceeded"
```

Можно комбинировать с временным фильтром:

```
_time:10m "error" kubernetes.pod_name:"nginx-log-generator"
```



## 5. Операторы пайплайна (часто используемые)

`filter` — пост-фильтрация результатов (обычно после `stats` или `math`):

```
| filter status:>=500
```

`fields` — выбор полей (аналог SELECT):

```
| fields _time, level, _msg, kubernetes.pod_name
```

`sort` — сортировка:

```
| sort by (_time desc)
| sort by (requests desc)
```

`limit` — ограничение количества строк:

```
| limit 10
| limit 5 by (errors desc)
```

`head` / `first` / `last` — (поддержка в разных версиях) — для получения первых/последних N элементов.



## 6. Извлечение данных и парсинг

`extract` — извлечение по регулярному выражению:

```
| extract "duration=(\d+)"
| extract "status=(?<status>\d+)"
```

`unpack_json` — распаковка JSON-поля в отдельные поля:

```
| unpack_json
| filter level:"ERROR"
```

`unpack_logfmt`, `unpack_syslog` и другие — для соответствующих форматов.

`replace`, `replace_regexp`, `pack_json`, `pack_logfmt` — для трансформаций и упаковки.



## 7. Агрегации и аналитика (`stats`)

`stats` — основной оператор агрегации.

```
| stats count()
| stats by (status) count() as requests
```

Функции: `count()`, `sum(field)`, `avg(field)`, `min(field)`, `max(field)`, `quantile(0.95, field)`, `count_uniq()`, `row_any()` и т.д.

Примеры:

- Количество запросов по статусам:

```
_time:5m | stats by (http.status_code) count() as requests
```

- Топ URL по трафику:

```
_time:5m | stats by (http.url) sum(http.bytes_sent) as bytes | sort by (bytes desc) | limit 10
```

- P95 latency:

```
_time:10m | stats quantile(0.95, request_time) as p95
```



## 8. Вычисления (`math`) и условия в агрегациях

`math` позволяет вычислять новые поля на основе существующих:

```
| math errors / total * 100 as error_rate
```

Условия внутри `stats` (через `if`):

```
| stats count() if (level:"ERROR") as error_count
```

Пример расчёта процента ошибок:

```
kubernetes.pod_namespace: "nginx-log-generator" |
stats
  count() as total,
  count() if (http.status_code:>=400) as errors |
math errors / total * 100 as error_rate
```



## 9. Практические паттерны

- Топ IP с ошибками:

```
_time:10m http.status_code:>=400 |
stats by (remote_addr) count() as errors |
sort by (errors desc) |
limit 10
```

- Медленные запросы:

```
_time:5m |
stats by (http.url) max(request_time) as max_time |
sort by (max_time desc) |
limit 5
```

- Поиск аномалий (много попыток входа):

```
_time:1h "failed login" |
stats by (user, ip) count() as attempts |
filter attempts:>20
```



## 10. Использование LogsQL в Grafana / VMUI

LogsQL поддерживается в VictoriaLogs datasource для Grafana и в VMUI:

- построение time-series графиков;
- таблицы с агрегациями;
- алерты на основе логов;
- единый язык запросов для VMUI и Grafana.



## 11. Cheatsheet (кратко)

| Операция          | Пример                         |
|-|--|
| Фильтр по времени | `_time:5m`                     |
| Поиск строки      | `"error"`                     |
| Фильтр поля       | `status:>=500`                 |
| JSON / распаковка | `| unpack_json`                |
| Regex extract     | `| extract "id=(\d+)"`       |
| Агрегация         | `| stats by (status) count()`   |
| Сортировка        | `| sort by (count desc)`        |
| Ограничение       | `| limit 10`                    |
| Вычисление        | `| math a / b * 100 as pct`     |

