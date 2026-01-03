### Фильтр eq_field

Иногда требуется найти логи, которые содержат одинаковые значения в заданных [полях](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Это можно сделать с помощью фильтра `field1:eq_field(field2)`.

Например, следующий запрос находит логи с одинаковыми значениями в полях `user_id` и `customer_id`:

```logsql
user_id:eq_field(customer_id)
```

Быстрый совет: используйте `NOT user_id:eq_field(customer_id)` для поиска логов, в которых `user_id` не равен `customer_id`. Здесь используется [логический оператор `NOT`](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

См. также:

* [фильтр `exact`](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
* [фильтр `le_field`](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
* [фильтр `lt_field`](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)
