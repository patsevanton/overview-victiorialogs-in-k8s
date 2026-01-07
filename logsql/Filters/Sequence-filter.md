## Фильтр последовательности

Находит сообщения логов, в которых слова или фразы идут в определённом порядке. По умолчанию применяется к полю `_msg`.

**Примеры:**

```logsql
seq("error", "open file")
event.original:seq(error, "open file")
"event:original":seq(error, "open file")
```
