## Замена подстроки (pipe replace)

Заменяет все вхождения подстроки на новую подстроку в указанном поле. Если замена в `_msg`, часть `at _msg` можно опустить. Поддерживает `limit N` и условную замену `if (...)`.

**Примеры:**

```logsql
_time:5m | replace ("secret-password", "***") at _msg
_time:5m | replace ("secret-password", "***")
_time:5m | replace ('foo', 'bar') at baz limit 1
_time:5m | replace if (user_type:=admin) ("secret", "***") at password
```
