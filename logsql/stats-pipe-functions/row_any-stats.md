## Статистика row_any

Возвращает произвольную запись лога (sample) для каждой выбранной группы статистики в виде JSON-кодированного словаря. Можно указать конкретные поля или префиксы.

**Примеры:**

```logsql
_time:5m | stats by (_stream) row_any() as sample_row
_time:5m | stats row_any(_time, path) as time_and_path_sample
_time:5m | stats row_any(prefix*)
```
