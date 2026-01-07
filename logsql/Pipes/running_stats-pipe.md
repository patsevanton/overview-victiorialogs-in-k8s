## Конвейер running_stats

Вычисляет накапливаемые статистики по указанным полям логов. Запрос должен возвращать поле `_time`. Поддерживает группировку `by (field1, ..., fieldM)`. Ключевое слово `by` можно опустить.

**Примеры:**

```logsql
_time:5m | running_stats sum(hits) as running_hits
_time:5m | running_stats count() as running_logs, sum(hits) as running_hits
_time:1d | stats by (_time:hour) count() as hits | running_stats sum(hits) as running_hits
_time:5m | running_stats by (host, path) count() running_logs, sum(hits) running_hits
```
