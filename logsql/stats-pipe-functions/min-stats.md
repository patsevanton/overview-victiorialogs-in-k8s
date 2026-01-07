## Статистика min

Возвращает минимальное значение среди указанных полей логов. Работает и со строковыми значениями. Поддерживает префиксы и условную статистику `if (...)`.

**Примеры:**

```logsql
_time:5m | stats min(duration) min_duration
_time:5m | stats min(prefix*)
_time:5m | stats min(some_field) if (some_field:*) as min_value_without_empty_string
```
