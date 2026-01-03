### row_min stats

`row_min(field)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) returns [log entry](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the minimum value for the given `field`. Log entry is returned as JSON-encoded dictionary with all the fields from the original log.

For example, the following query returns log entry with the minimum value for the `duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
across logs for the last 5 minutes:

```logsql
_time:5m | stats row_min(duration) as log_with_min_duration
```

Fields from the returned values can be decoded with [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) or [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pipes.

If only the specific fields are needed from the returned log entry, then they can be enumerated inside `row_max(...)`.
For example, the following query returns only `_time`, `path` and `duration` fields from the log entry with the minimum `duration` over the last 5 minutes:

```logsql
_time:5m | stats row_min(duration, _time, path, duration) as time_and_path_with_min_duration
```

It is possible to return all the fields starting with particular prefix by using `row_min(field, prefix*)` syntax.
