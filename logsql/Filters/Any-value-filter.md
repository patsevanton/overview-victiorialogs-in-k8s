### Фильтр «любое значение»

Иногда требуется найти записи журнала, содержащие **любое непустое значение** для заданного [поля журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Это можно сделать с помощью синтаксиса `log_field:*`. Например, следующий запрос отбирает записи журнала с непустым полем `host.hostname`:

```logsql
host.hostname:*
```

Смотрите также:

- [Фильтр «без операции»](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
- [Фильтр пустого значения](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter)
- [Фильтр по префиксу](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
