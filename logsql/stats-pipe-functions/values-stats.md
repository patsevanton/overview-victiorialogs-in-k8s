## Статистика values

Возвращает все значения (включая пустые) для указанных полей логов в виде JSON-массива. Поддерживает префиксы.

**Примеры:**

```logsql
_time:5m | stats values(ip) ips
_time:5m | stats values(prefix*)
```
