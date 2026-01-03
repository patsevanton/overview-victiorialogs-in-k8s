### values stats

`values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns all the values (including empty values)
for the mentioned [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
The returned values are encoded in JSON array.

For example, the following query returns all the values for the `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | stats values(ip) ips
```

The returned IP addresses can be unrolled into distinct log entries with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

It is possible to get values for all the fields with common prefix via `values(prefix*)` syntax.
