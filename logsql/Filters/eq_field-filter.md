### eq_field filter

Sometimes it is needed to find logs, which contain identical values in the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be done with `field1:eq_field(field2)` filter.

For example, the following query matches logs with identical values at `user_id` and `customer_id` fields:

```logsql
user_id:eq_field(customer_id)
```

Quick tip: use `NOT user_id:eq_field(customer_id)` for finding logs where `user_id` isn't equal to `customer_id`. It uses [`NOT` logical operator](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).

See also:

- [`exact` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)

