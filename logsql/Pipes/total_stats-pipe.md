## Конвейер total_stats

Вычисляет общие (глобальные) статистические показатели по указанным полям логов. Запрос должен возвращать поле `_time`. Поддерживает группировку `by (field1, ..., fieldM)`. Ключевое слово `by` можно опустить.

**Примеры:**

```logsql
_time:5m | total_stats sum(hits) as total_hits
_time:5m | total_stats count() as total_logs, sum(hits) as total_hits
_time:1d | stats by (_time:hour) count() as hits | total_stats sum(hits) as total_hits | math round((hits / total_hits)*100) as hits_percent
_time:5m | total_stats by (host, path) count() total_logs, sum(hits) total_hits
```
