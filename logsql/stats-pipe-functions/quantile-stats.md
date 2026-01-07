## Статистика quantile

Вычисляет приближённый phi-й процентиль по значениям указанных полей логов. Параметр phi должен быть в диапазоне 0...1. Работает и со строковыми значениями. Поддерживает префиксы и условную статистику `if (...)`.

**Примеры:**

```logsql
_time:5m | stats quantile(0.5, request_duration_seconds) p50, quantile(0.9, request_duration_seconds) p90, quantile(0.99, request_duration_seconds) p99
_time:5m | stats quantile(phi, prefix*)
_time:5m | stats quantile(phi, some_field) if (some_field:*) as quantile_without_empty_string
```
