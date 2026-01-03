### sum_len stats

`sum_len(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the sum of byte lengths of all the values
for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the sum of byte lengths of [`_msg` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
across all the logs for the last 5 minutes:

```logsql
_time:5m | stats sum_len(_msg) messages_len
```

It is possible to find the sum of byte lengths for all the fields with common prefix via `sum_len(prefix*)` syntax.
