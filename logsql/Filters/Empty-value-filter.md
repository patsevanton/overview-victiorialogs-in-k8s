### Фильтр пустого значения

Иногда требуется найти записи логов без указанного [поля лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Это можно сделать с помощью синтаксиса `log_field:""`. Например, следующий запрос находит записи логов без поля `host.hostname`:

```logsql
host.hostname:""
```

См. также:

* [Фильтр без операции (No-op filter)](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
* [Фильтр любого значения (Any value filter)](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter)
* [Фильтр по слову (Word filter)](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
* [Логический фильтр (Logical filter)](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
