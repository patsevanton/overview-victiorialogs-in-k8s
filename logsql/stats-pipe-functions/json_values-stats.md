### json_values stats

`json_values(field1, ..., fieldN)` [stats pipe function](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions) packs the given fields into JSON for every log entry and returns a JSON array,
which can be unrolled with [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe).

For example, the following query returns per-`app` JSON arrays containing [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
and [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) fields for the last 5 minutes:

```logsql
_time:5m | stats by (app) json_values(_time, _msg) as json_logs
```

If the list of fields is empty, then all the log fields are encoded into a JSON array:

```logsql
_time:5m | stats json_values() as json_logs
```

It is possible to select values with the given prefix via `json_values(prefix*)` syntax.

It is possible to set the upper limit on the number of JSON-encoded logs with the `limit N` suffix. For example, the following query
returns up to 3 JSON-encoded logs for every `host`:

```logsql
_time:5m | stats by (host) json_values() limit 3 as json_logs
```

It is possible to sort the selected log entries by appending `sort by (...)`. For example, the following query returns per-`host` logs
over the last 5 minutes sorted by descending order of [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | stats by (host) json_values() sort by (_time desc) as json_logs
```

The `sort by (...)` allows selecting top N logs for each group when combined with `limit N`. For example, the following query selects up to 3 of the most recent logs for every `host`
over the last 5 minutes:

```logsql
_time:5m | stats by (host) json_values() sort by (_time desc) limit 3 as json_logs
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
- [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
- [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)
- [`values`](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)

