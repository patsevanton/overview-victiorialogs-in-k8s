### avg stats

`avg(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the average value across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Non-numeric values are ignored. If all the values are non-numeric, then `NaN` is returned.

For example, the following query returns the average value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats avg(duration) avg_duration
```

It is possible to calculate the average over fields with common prefix via `avg(prefix*)` syntax. For example, the following query calculates the average
over all the log fields with `foo` prefix:

```logsql
_time:5m | stats avg(foo*)
```

See also:

- [`median`](https://docs.victoriametrics.com/victorialogs/logsql/#median-stats)
- [`quantile`](https://docs.victoriametrics.com/victorialogs/logsql/#quantile-stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

