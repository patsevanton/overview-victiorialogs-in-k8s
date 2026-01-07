## Последний конвейер (last pipe)

Возвращает последние N записей журнала после сортировки по указанным полям. Поддерживает `partition by` для группировки.

**Примеры:**

```logsql
_time:5m | last 10 by (request_duration)
_time:1h | last 3 by (request_duration) partition by (host)
```
