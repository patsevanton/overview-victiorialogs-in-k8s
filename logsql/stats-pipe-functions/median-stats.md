## Статистика median

Вычисляет оценочное значение медианы по указанным полям логов. Работает и со строковыми значениями. Поддерживает префиксы и условную статистику `if (...)`.

**Примеры:**

```logsql
_time:5m | stats median(duration) median_duration
_time:5m | stats median(prefix*)
_time:5m | stats median(some_field) if (some_field:*) as median_without_empty_string
```
