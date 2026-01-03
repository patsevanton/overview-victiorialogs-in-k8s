### count_empty stats

`count_empty(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of logs with empty `(field1, ..., fieldN)` tuples.

For example, the following query calculates the number of logs with empty `username` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
during the last 5 minutes:

```logsql
_time:5m | stats count_empty(username) logs_with_missing_username
```

It is possible to calculate the number of logs with empty fields with common prefix via `count_empty(prefix*)` syntax. For example, the following query
calculates the number of logs with empty fields with `foo` prefix during the last 5 minutes:

```logsql
_time:5m | stats count_empty(foo*)
```

See also:

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)

