## Статистика row_min

Возвращает запись лога с минимальным значением для указанного поля в виде JSON-кодированного словаря. Можно указать конкретные поля или префиксы.

**Примеры:**

```logsql
_time:5m | stats row_min(duration) as log_with_min_duration
_time:5m | stats row_min(duration, _time, path, duration) as time_and_path_with_min_duration
_time:5m | stats row_min(field, prefix*)
```
