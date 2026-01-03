### row_any stats

`row_any()` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns an arbitrary [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
(aka sample) for each selected [stats group](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields). The log entry is returned as a JSON-encoded dictionary with all the fields from the original log.

For example, the following query returns a sample log entry for each [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
across logs for the last 5 minutes:

```logsql
_time:5m | stats by (_stream) row_any() as sample_row
```

Fields from the returned values can be decoded with [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) or [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pipes.

If only the specific fields are needed, then they can be enumerated inside `row_any(...)`.
For example, the following query returns only `_time` and `path` fields from a sample log entry for logs over the last 5 minutes:

```logsql
_time:5m | stats row_any(_time, path) as time_and_path_sample
```

It is possible to return all the fields starting with particular prefix by using `row_any(prefix*)` syntax.

See also:

- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`json_values`](https://docs.victoriametrics.com/victorialogs/logsql/#json_values-stats)

