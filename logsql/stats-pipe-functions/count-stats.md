## Статистика count

Вычисляет количество выбранных логов. Можно указать поля для подсчёта логов с непустыми значениями. Поддерживает несколько полей и префиксы.

**Примеры:**

```logsql
_time:5m | stats count() logs
_time:5m | stats count(username) logs_with_username
_time:5m | stats count(username, password) logs_with_username_or_password
_time:5m | stats count(foo*)
```
