## Пайп unpack_logfmt

Распаковывает поля формата logfmt (`k1=v1 ... kN=vN`) из указанного поля. Если применяется к `_msg`, часть `from _msg` можно опустить. Поддерживает `fields (...)`, `keep_original_fields`, `skip_empty_results`, условную распаковку `if (...)`.

**Примеры:**

```logsql
_time:5m | unpack_logfmt from _msg
_time:5m | unpack_logfmt
_time:5m | unpack_logfmt from my_logfmt fields (foo, bar)
_time:5m | unpack_logfmt from foo fields (ip, host) keep_original_fields
_time:5m | unpack_logfmt fields (ip, host) skip_empty_results
_time:5m | unpack_logfmt if (ip:"") from foo
```
