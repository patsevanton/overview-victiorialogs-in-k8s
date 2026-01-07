## Конвейер top

Возвращает топ-N наборов значений по полям, которые встречаются чаще всего. Параметр N необязателен (по умолчанию 10). Поддерживает `hits as`, `rank`.

**Примеры:**

```logsql
_time:5m | top 7 by (_stream)
_time:5m | top by (ip)
_time:5m | top by (path) hits as visits
_time:5m | top 10 by (ip) rank
_time:5m | top 10 by (ip) rank as position
```
