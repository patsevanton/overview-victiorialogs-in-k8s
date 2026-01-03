### Конвейер `first`

Конвейер `<q> | first N by (fields)` ([документация](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)) возвращает первые `$N$` записей журнала из запроса `<q>` ([синтаксис запросов](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)) после их сортировки по указанным полям (`fields`) ([модель данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)).

**Пример.** Следующий запрос возвращает первые 10 записей журнала с наименьшим значением поля `request_duration` за последние 5 минут:

```logsql
_time:5m | first 10 by (request_duration)
```

Можно вернуть до `$N$` записей индивидуально для каждой группы записей с одинаковым набором полей, перечислив этот набор в `partition by (...)`.

**Пример.** Следующий запрос возвращает до 3 записей с наименьшим `request_duration` для каждого хоста за последний час:

```logsql
_time:1h | first 3 by (request_duration) partition by (host)
```
