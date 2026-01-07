## Устранение неполадок (Troubleshooting)

Самая частая причина медленных запросов — запрос слишком большого количества логов без достаточной фильтрации. Всегда **будьте максимально конкретны** при построении запросов.

### Проверьте, сколько логов соответствует вашему запросу

Добавляйте `| count()` после каждого фильтра или pipe, чтобы увидеть количество совпадающих логов.

**Примеры:**

```logsql
_time:5m host:"api-" level:error "database" | count()
_time:5m level:error | count()
_time:5m host:"api-" | count()
```

Фильтр `_time` является обязательным: если его нет, VictoriaLogs сканирует **все** логи, хранящиеся в базе данных.

### Проверяйте использование stream-фильтров в запросе

Используйте правильный синтаксис stream-фильтров:

```logsql
{app="nginx"}
```

Вместо:

```logsql
app:=nginx
```

### Проверьте количество уникальных log stream'ов

**Примеры:**

```logsql
_time:1d | count_uniq(_stream_id)
_time:1d | top 10 by (_stream)
_time:1d {app="nginx"} | stats count_uniq(_stream) as streams, count() as logs
```

### Определите самые «дорогие» части запроса

Используйте `block_stats` для анализа:

```logsql
_time:1d | keep kubernetes.pod_name, kubernetes.pod_namespace | block_stats
_time:1d | keep kubernetes.pod_name, kubernetes.pod_namespace | block_stats | stats by (field) sum(values_bytes) values_bytes_on_disk, sum(rows) rows | sort by (values_bytes_on_disk) desc
```

### Профилируйте pipes поэтапно

Добавляйте фильтры и pipes по одному, измеряя производительность:

```logsql
_time:5m | count()
_time:5m error | count()
_time:5m error -"cannot open file" | count()
_time:5m error contains_any("access denied", "unauthorized", "403") | count()
```

**Рекомендации по оптимизации:**

- Сопоставление по regex и парсинг JSON — дорогие операции. Используйте более быстрые альтернативы.
- Сортировка без ограничения (`sort` без `limit`) сохраняет все логи в памяти. Добавьте `limit` или уменьшите входной объём данных.
- Функции с высокой кардинальностью, такие как `count_uniq()`, хранят в памяти все уникальные значения.
- Большое число групп в `stats by (...)` может потреблять много памяти.
