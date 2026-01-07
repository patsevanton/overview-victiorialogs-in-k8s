## Конвейер replace_regexp

Заменяет подстроки, соответствующие регулярному выражению RE2, на строку замены. В строке замены можно использовать плейсхолдеры `$N` или `${N}`. Если замена в `_msg`, часть `at _msg` можно опустить. Поддерживает `limit N` и условную замену `if (...)`.

**Примеры:**

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1") at _msg
_time:5m | replace_regexp ("host-(.+?)-foo", "$1")
_time:5m | replace_regexp ('password: [^ ]+', '') at baz limit 1
_time:5m | replace_regexp if (user_type:=admin) ("password: [^ ]+", "***") at foo
```
