## Удалить поля (delete pipe)

Удаляет указанные поля из логов. Можно использовать `drop`, `del`, `rm` вместо `delete`. Поддерживает удаление полей с общим префиксом.

**Примеры:**

```logsql
_time:5m | delete host, app
_time:5m | drop host
_time:5m | delete foo*
```
