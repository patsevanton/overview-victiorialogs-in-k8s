## Статистика row_max

Возвращает запись лога с максимальным значением для указанного поля в виде JSON-кодированного словаря. Можно указать конкретные поля или префиксы.

**Примеры:**

```logsql
_time:5m | stats row_max(duration) as log_with_max_duration
_time:5m | stats row_max(duration, _time, path, duration) as time_and_path_with_max_duration
_time:5m | stats row_max(field, prefix*)
```
