## Конвейер first

Возвращает первые N записей журнала после сортировки по указанным полям. Поддерживает `partition by` для группировки.

**Примеры:**

```logsql
_time:5m | first 10 by (request_duration)
_time:1h | first 3 by (request_duration) partition by (host)
```
