### time_add pipe

`<q> | time_add <duration>` adds the given `<duration>` to the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
The `<duration>` can be in any format described [here](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).

For example, the following query adds one hour to `_time` field in the selected logs:

```logsql
_time:5m | time_add 1h
```

Specify negative duration for subtracting it from the `_time` field:

```logsql
_time:5m | time_add -1h
```

Add `at <field_name>` to the end of the `time_add` pipe in order to add the given `<duration>` to the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the given `<field_name>`. For example, the following query adds one week to the field `transaction_time`:

```logsql
_time:5m | time_add 1w at transaction_time
```

See also:

- [`_time` filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter).
- [`time_offset` option](https://docs.victoriametrics.com/victorialogs/logsql/#query-options).

