## Статистика rate_sum

Возвращает среднюю скорость в секунду для суммы по указанным числовым полям. Поддерживает префиксы.

**Примеры:**

```logsql
_time:5m | stats rate_sum(bytes_sent)
_time:5m | stats rate_sum(prefix*)
```
