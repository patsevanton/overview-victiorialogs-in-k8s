## Конвейер field_values

Возвращает все значения для указанного поля вместе с количеством логов для каждого значения. Поддерживает `limit N`.

**Примеры:**

```logsql
_time:5m | field_values level
_time:5m | field_values user_id limit 10
```
