## total_stats pipe functions

LogsQL supports the following functions for [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe):

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats) returns the number of log entries.
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-total_stats) returns the maximum value over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-total_stats) returns the minimum value over the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats) returns the sum for the given numeric [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

### count total_stats

`count()` [`total_stats` pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions) calculates the total number of selected logs.

For example, the following query adds the `total_logs` field to the selected logs over the last 5 minutes:

```logsql
_time:5m | total_stats count() total_logs
```

It is possible to calculate the number of logs with non-empty values for some [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the `count(fieldName)` syntax. For example, the following query returns the total number of logs with non-empty `username` field over the last 5 minutes:

```logsql
_time:5m | total_stats count(username) total_logs_with_username
```

If multiple fields are enumerated inside `count()`, then it counts the number of logs with at least a single non-empty field mentioned inside `count()`.
For example, the following query returns the number of logs with non-empty `username` or `password` [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | total_stats count(username, password) total_logs_with_username_or_password
```

It is possible to calculate the number of logs with at least a single non-empty field with common prefix with `count(prefix*)` syntax.
For example, the following query returns the number of logs with at least a single non-empty field with `foo` prefix over the last 5 minutes:

```logsql
_time:5m | total_stats count(foo*)
```

See also:

- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-total_stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-total_stats)

### max total_stats

`max(field1, ..., fieldN)` [`total_stats` pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions) returns the total maximum across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the total maximum for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | total_stats max(duration) total_max_duration
```

It is possible to calculate the total maximum value across all the fields with common prefix via `max(prefix*)` syntax.

See also:

- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-total_stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats)

### min total_stats

`min(field1, ..., fieldN)` [`total_stats` pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions) returns the total minimum across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the total minimum for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | total_stats min(duration) total_min_duration
```

It is possible to find the total minimum across all the fields with common prefix via `min(prefix*)` syntax.

See also:

- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-total_stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats)

### sum total_stats

`sum(field1, ..., fieldN)` [`total_stats` pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions) calculates the total sum of numeric values across
all the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
Non-numeric values are skipped. If all the values across `field1`, ..., `fieldN` are non-numeric, then `NaN` is returned.

For example, the following query returns the total sum of numeric values for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | total_stats sum(duration) total_sum_duration
```

It is possible to find the total sum for all the fields with common prefix via `sum(prefix*)` syntax.

See also:

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-total_stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-total_stats)

