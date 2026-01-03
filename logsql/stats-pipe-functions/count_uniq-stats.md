### count_uniq stats

`count_uniq(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of unique non-empty `(field1, ..., fieldN)` tuples.

For example, the following query returns the number of unique non-empty values for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq(ip) ips
```

The following query returns the number of unique `(host, path)` pairs for the corresponding [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq(host, path) unique_host_path_pairs
```

Every unique value is stored in memory during query execution. A large number of unique values may require a lot of memory.
Sometimes it is necessary to know whether the number of unique values reaches a limit. In this case add `limit N` just after `count_uniq(...)`
for limiting the number of counted unique values up to `N`, while limiting the maximum memory usage. For example, the following query counts
up to `1_000_000` unique values for the `ip` field:

```logsql
_time:5m | stats count_uniq(ip) limit 1_000_000 as ips_1_000_000
```

If it is OK to count an estimated number of unique values, then [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats) can be used as faster alternative to `count_uniq`.

See also:

- [`count_uniq_hash`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq_hash-stats)
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

