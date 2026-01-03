### Фильтр пустого значения

Иногда требуется найти записи логов без указанного [поля лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Это можно сделать с помощью синтаксиса `log_field:""`. Например, следующий запрос находит записи логов без поля `host.hostname`:

```logsql
host.hostname:""
```
