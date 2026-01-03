### count_uniq_hash stats

`count_uniq_hash(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) calculates the number of unique hashes for non-empty `(field1, ..., fieldN)` tuples.
This is a good estimate for the number of unique values in the general case, while it works faster and uses less memory than [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
when counting a large number of unique values.

For example, the following query returns an estimated number of unique non-empty values for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq_hash(ip) unique_ips_count
```

The following query returns an estimated number of unique `(host, path)` pairs for the corresponding [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | stats count_uniq_hash(host, path) unique_host_path_pairs
```

See also:

- [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)
- [`uniq_values`](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats)

