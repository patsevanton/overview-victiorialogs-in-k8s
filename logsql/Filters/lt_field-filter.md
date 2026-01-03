### lt_field filter

Sometimes it is needed to find logs where one [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value is smaller than the other field value.
This can be done with `field1:lt_field(field2)` filter.

For example, the following query matches logs where `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) is smaller than the `max_duration` field:

```logsql
duration:lt_field(max_duration)
```

Quick tip: use `NOT duration:lt_field(max_duration)` for finding logs where `duration` is bigger or equal to the `max_duration`.

See also:

- [range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`eq_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)

