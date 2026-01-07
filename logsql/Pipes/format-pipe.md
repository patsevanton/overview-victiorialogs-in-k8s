## Труба format (format pipe)

Объединяет поля логов согласно шаблону и сохраняет результат в поле. Если результат сохраняется в `_msg`, часть `as _msg` можно опустить. Поддерживает префиксы: `duration_seconds:`, `q:`, `uc:`, `lc:`, `urlencode:`, `urldecode:`, `hexencode:`, `hexdecode:`, `base64encode:`, `base64decode:`, `hexnumdecode:`, `time:`, `duration:`, `ipv4:`, `hexnumencode:`. Поддерживает `keep_original_fields`, `skip_empty_results`, условное форматирование `if (...)`.

**Примеры:**

```logsql
_time:5m | format "request from <ip>:<port>" as _msg
_time:5m | format "request from <ip>:<port>"
_time:5m | format '{"_msg":<q:_msg>,"stacktrace":<q:stacktrace>}' as my_json
_time:5m | format 'uppercase foo: <uc:foo>, lowercase bar: <lc:bar>' as result
_time:5m | format 'url: http://foo.com/?user=<urlencode:user>'
_time:5m | format if (ip:* and host:*) "request from <ip>:<host>" as message
```
