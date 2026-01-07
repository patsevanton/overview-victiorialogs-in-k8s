## Статистика json_values

Упаковывает указанные поля в JSON для каждой записи лога и возвращает JSON-массив. Поддерживает пустой список полей (все поля), префиксы, `limit N`, `sort by (...)`.

**Примеры:**

```logsql
_time:5m | stats by (app) json_values(_time, _msg) as json_logs
_time:5m | stats json_values() as json_logs
_time:5m | stats by (host) json_values() limit 3 as json_logs
_time:5m | stats by (host) json_values() sort by (_time desc) limit 3 as json_logs
```
