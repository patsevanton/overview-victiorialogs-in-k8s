### uniq_values stats

`uniq_values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns the unique non-empty values across
the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
The returned values are encoded in sorted JSON array.

For example, the following query returns unique non-empty values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats uniq_values(ip) unique_ips
```

The returned unique IP addresses can be unrolled into distinct log entries with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

Every unique value is stored in memory during query execution. Big number of unique values may require a lot of memory. Sometimes it is enough to return
only a subset of unique values. In this case add `limit N` after `uniq_values(...)` in order to limit the number of returned unique values to `N`,
while limiting the maximum memory usage.
For example, the following query returns up to `100` unique values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the logs for the last 5 minutes:

```logsql
_time:5m | stats uniq_values(ip) limit 100 as unique_ips_100
```

Arbitrary subset of unique `ip` values is returned every time if the `limit` is reached.

It is possible to find unique values for all the fields with common prefix via `uniq_values(prefix*)` syntax.
