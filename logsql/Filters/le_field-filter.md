### Фильтр `le_field`

Иногда требуется найти логи, в которых значение одного [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) не превышает значение другого поля.  
Это можно сделать с помощью фильтра `field1:le_field(field2)`.

Например, следующий запрос отбирает логи, в которых значение поля `duration` [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) не превышает значения поля `max_duration`:

```logsql
duration:le_field(max_duration)
```

Полезный совет: используйте `NOT duration:le_field(max_duration)`, чтобы найти логи, в которых `duration` превышает `max_duration`.

Смотрите также:

- [фильтр сравнения диапазонов](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter);
- фильтр [`lt_field`](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter);
- фильтр [`eq_field`](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter).
