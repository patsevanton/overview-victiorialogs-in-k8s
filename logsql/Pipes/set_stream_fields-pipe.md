## Конвейер set_stream_fields

Задаёт указанные поля логов в качестве полей `_stream`. Поддерживает условное применение `if (...)`.

**Примеры:**

```logsql
_time:5m | set_stream_fields host, path
_time:5m | set_stream_fields if (host:="foobar") host, app
```
