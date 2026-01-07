## Конвейер pack_logfmt

Упаковывает все поля записи журнала в сообщение формата logfmt и сохраняет в виде строки. Если результат сохраняется в `_msg`, часть `as _msg` можно опустить. Поддерживает `fields (...)` для выбора полей.

**Примеры:**

```logsql
_time:5m | pack_logfmt as _msg
_time:5m | pack_logfmt
_time:5m | pack_logfmt fields (foo, bar) as baz
_time:5m | pack_logfmt fields (foo.*, bar.*) as baz
_time:5m | pack_logfmt as foo | fields foo
```
