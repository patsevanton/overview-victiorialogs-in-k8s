## Конвейер extract_regexp

Извлекает подстроки из поля согласно регулярному выражению RE2 с именованными группами `(?P<capture_field_name>...)`. Если применяется к `_msg`, часть `from _msg` можно опустить.

**Примеры:**

```logsql
_time:5m | extract_regexp "(?P<ip>([0-9]+[.]){3}[0-9]+)" from _msg
_time:5m | extract_regexp "(?P<ip>([0-9]+[.]){3}[0-9]+)"
_time:5m | extract_regexp 'ip=(?P<ip>([0-9]+[.]){3}[0-9]+)' keep_original_fields
_time:5m | extract_regexp 'ip=(?P<ip>([0-9]+[.]){3}[0-9]+)' from foo skip_empty_results
_time:5m | extract_regexp if (ip:"") "ip=(?P<ip>([0-9]+[.]){3}[0-9]+)"
```
