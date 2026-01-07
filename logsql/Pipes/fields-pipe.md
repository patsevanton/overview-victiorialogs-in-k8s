## Конвейер fields (выбор полей)

Выбирает конкретный набор полей лога. Можно использовать `keep` вместо `fields`. Поддерживает шаблоны с подстановкой.

**Примеры:**

```logsql
_time:5m | fields host, _msg
_time:5m | keep host, _msg
_time:5m | fields foo*
```
