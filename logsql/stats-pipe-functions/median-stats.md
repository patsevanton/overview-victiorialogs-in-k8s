### median stats

`median(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the estimated [median](https://en.wikipedia.org/wiki/Median) value across
the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query return median for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats median(duration) median_duration
```

The `median(some_field)` function works with string values for the `some_field`, so it returns an empty string value if `some_field`
is missing in some of the processed logs according to [VictoriaLogs data model](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Use `median(some_field) if (some_field:*) as min_value_without_empty_string` syntax for filtering out empty string values.
See [conditional stats docs](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) for more details.

It is possible to calculate the median across all the fields with common prefix via `median(prefix*)` syntax.
