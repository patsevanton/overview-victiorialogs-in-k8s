## Пайп unpack_json

Распаковывает JSON из указанного поля в выходные поля. Если применяется к `_msg`, часть `from _msg` можно опустить. Поддерживает `fields (...)`, `keep_original_fields`, `skip_empty_results`, условную распаковку `if (...)`.

**Примеры:**

```logsql
_time:5m | unpack_json from _msg
_time:5m | unpack_json
_time:5m | unpack_json from my_json fields (foo, bar)
_time:5m | unpack_json from foo fields (ip, host) keep_original_fields
_time:5m | unpack_json fields (ip, host) skip_empty_results
_time:5m | unpack_json if (ip:"") from foo
```
