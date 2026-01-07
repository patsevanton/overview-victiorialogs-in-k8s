## Конвейер drop_empty_fields

Удаляет поля с пустыми значениями из результатов. Пропускает записи журнала, в которых нет ни одного непустого поля.

**Примеры:**

```logsql
_time:5m | extract 'email: <email>,' from foo | drop_empty_fields
```
