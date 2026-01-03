### rate_sum stats

`rate_sum(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the average per-second rate of the sum over the given
numeric [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the average per-second rate of the sum of `bytes_sent` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats rate_sum(bytes_sent)
```

It is possible to calculate the average per-second rate of the sum over all the fields starting with a particular prefix by using `rate_sum(prefix*)` syntax.

See also:

- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-stats)
- [`rate`](https://docs.victoriametrics.com/victorialogs/logsql/#rate-stats)

