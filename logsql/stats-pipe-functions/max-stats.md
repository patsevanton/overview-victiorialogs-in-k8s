## Статистика max

Возвращает максимальное значение среди указанных полей логов. Работает и со строковыми значениями. Поддерживает префиксы и условную статистику `if (...)`.

**Примеры:**

```logsql
_time:5m | stats max(duration) max_duration
_time:5m | stats max(prefix*)
_time:5m | stats max(some_field) if (some_field:*) as max_value_without_empty_string
```
