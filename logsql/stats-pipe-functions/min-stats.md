### min stats

`min(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the minimum value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the minimum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats min(duration) min_duration
```

The `min(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `min(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to find the minimum across all the fields with common prefix via `min(prefix*)` syntax.

[`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats) function can be used for obtaining other fields with the minimum duration.
