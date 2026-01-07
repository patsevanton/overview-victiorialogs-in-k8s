## Конвейер pack_json

Упаковывает все поля записи журнала в объект JSON и сохраняет в виде строки. Если результат сохраняется в `_msg`, часть `as _msg` можно опустить. Поддерживает `fields (...)` для выбора полей.

**Примеры:**

```logsql
_time:5m | pack_json as _msg
_time:5m | pack_json
_time:5m | pack_json fields (foo, bar) as baz
_time:5m | pack_json fields (foo.*, bar.*) as baz
_time:5m | pack_json as foo | fields foo
```
