### le_field filter

Sometimes it is needed to find logs where one [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) value doesn't exceed the other field value.
This can be done with `field1:le_field(field2)` filter.

For example, the following query matches logs where `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) doesn't exceed the `max_duration` field:

```logsql
duration:le_field(max_duration)
```

Quick tip: use `NOT duration:le_field(max_duration)` for finding logs where `duration` exceeds the `max_duration`.

See also:

- [range comparison filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)
- [`eq_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)

