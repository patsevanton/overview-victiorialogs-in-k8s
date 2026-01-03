### sum stats

`sum(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the sum of numeric values across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Non-numeric values are skipped. If all the values across `field1`, ..., `fieldN` are non-numeric, then `NaN` is returned.

For example, the following query returns the sum of numeric values for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats sum(duration) sum_duration
```

It is possible to find the sum for all the fields with common prefix via `sum(prefix*)` syntax.
