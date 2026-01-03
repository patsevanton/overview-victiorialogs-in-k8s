### count stats

`count()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of selected logs.

For example, the following query returns the number of logs over the last 5 minutes:

```logsql
_time:5m | stats count() logs
```

It is possible to calculate the number of logs with non-empty values for some [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the `count(fieldName)` syntax. For example, the following query returns the number of logs with non-empty `username` field over the last 5 minutes:

```logsql
_time:5m | stats count(username) logs_with_username
```

If multiple fields are enumerated inside `count()`, then it counts the number of logs with at least a single non-empty field mentioned inside `count()`.
For example, the following query returns the number of logs with non-empty `username` or `password` [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count(username, password) logs_with_username_or_password
```

It is possible to calculate the number of logs with at least a single non-empty field with common prefix with `count(prefix*)` syntax.
For example, the following query returns the number of logs with at least a single non-empty field with `foo` prefix over the last 5 minutes:

```logsql
_time:5m | stats count(foo*)
```

See also:

- [`rate`](https://docs.victoriametrics.com/victorialogs/logsql/#rate-stats)
- [`rate_sum`](https://docs.victoriametrics.com/victorialogs/logsql/#rate_sum-stats)
- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
- [`count_empty`](https://docs.victoriametrics.com/victorialogs/logsql/#count_empty-stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`avg`](https://docs.victoriametrics.com/victorialogs/logsql/#avg-stats)

