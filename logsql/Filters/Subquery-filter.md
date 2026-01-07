## Фильтр с подзапросом

Отбирает логи, в которых значения полей совпадают со значениями, полученными в результате подзапроса. Подзапрос должен завершаться конвейером `fields` или `uniq` с одним полем.

**Примеры:**

```logsql
_time:5m AND user_id:in(_time:1d AND path:admin | fields user_id)
_time:5m _msg:contains_all(_time:1d is_admin:true | fields user_id)
_time:5m _msg:contains_any(_time:1d is_admin:true | fields user_id)
```
