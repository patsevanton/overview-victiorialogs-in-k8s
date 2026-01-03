### Конвейер `drop_empty_fields`

Конвейер `<q> | drop_empty_fields` удаляет [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с пустыми значениями из результатов, возвращаемых запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).  
Кроме того, он пропускает записи журнала, в которых нет ни одного непустого поля.

Например, следующий запрос удалит возможное пустое поле `email`, сформированное конвейером [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe), если поле `foo` не содержит адреса электронной почты:

```logsql
_time:5m | extract 'email: <email>,' from foo | drop_empty_fields
```
