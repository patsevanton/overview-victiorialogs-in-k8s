## Пайп unpack_syslog

Распаковывает сообщения syslog (RFC3164, RFC5424) из указанного поля. Если применяется к `_msg`, часть `from _msg` можно опустить. Поддерживает `offset`, `keep_original_fields`, `result_prefix`, условную распаковку `if (...)`.

**Примеры:**

```logsql
_time:5m | unpack_syslog from _msg
_time:5m | unpack_syslog
_time:5m | unpack_syslog offset 5h30m
_time:5m | unpack_syslog keep_original_fields
_time:5m | unpack_syslog from foo result_prefix "foo_"
_time:5m | unpack_syslog if (hostname:"") from foo
```
