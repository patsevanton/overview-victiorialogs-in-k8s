### Фильтр с подзапросом

Иногда требуется отобрать логи, в которых значения [полей](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) совпадают со значениями, полученными в результате другого [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) (так называемого *подзапроса*). В LogsQL для этого предусмотрены следующие фильтры:

- `field:in(<подзапрос>)` — возвращает логи, в которых значения поля `field` совпадают со значениями, возвращёнными `<подзапросом>`.  
  Например, следующий запрос выбирает все логи за последние 5 минут для пользователей, которые за последний день посещали страницы, содержащие слово `admin` в поле `path`:

  ```logsql
  _time:5m AND user_id:in(_time:1d AND path:admin | fields user_id)
  ```

- `field:contains_all(<подзапрос>)` — возвращает логи, в которых значение поля `field` содержит **все** слова и фразы, возвращённые `<подзапросом>`.  
  Например, следующий запрос выбирает все логи за последние 5 минут, которые содержат **все** значения `user_id` из административных логов за последний день в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_all(_time:1d is_admin:true | fields user_id)
  ```

- `field:contains_any(<подзапрос>)` — возвращает логи, в которых значение поля `field` содержит **хотя бы одно** слово или фразу, возвращённую `<подзапросом>`.  
  Например, следующий запрос выбирает все логи за последние 5 минут, которые содержат **хотя бы одно** значение `user_id` из административных логов за последний день в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

  ```logsql
  _time:5m _msg:contains_any(_time:1d is_admin:true | fields user_id)
  ```

`<подзапрос>` должен завершаться либо конвейером [`fields`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe), либо конвейером [`uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe), содержащим имя **одного** поля. Это нужно, чтобы VictoriaLogs могла использовать значения этого поля для сопоставления с заданным фильтром.

См. также:

- фильтр [`in`](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter);
- фильтр [`contains_all`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter);
- фильтр [`contains_any`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter);
- конвейер [`join`](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe);
- конвейер [`union`](https://docs.victoriametrics.com/victorialogs/logsql/#union-pipe).
