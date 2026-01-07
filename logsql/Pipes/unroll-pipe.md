## Пайп unroll

Разворачивает JSON-массивы из полей лога в отдельные строки. Поддерживает условное применение `if (...)`.

**Примеры:**

```logsql
_time:5m | unroll (timestamp, value)
_time:5m | unroll if (value_type:="json_array") (value)
```
