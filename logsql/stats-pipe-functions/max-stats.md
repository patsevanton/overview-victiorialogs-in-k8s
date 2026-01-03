### max stats

`max(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the maximum value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the maximum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats max(duration) max_duration
```

The `max(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `max(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to calculate the maximum value across all the fields with common prefix via `max(prefix*)` syntax.

[`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats) function can be used for obtaining other fields with the maximum duration.
