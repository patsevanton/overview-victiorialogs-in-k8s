### total_stats pipe

The `<q> | total_stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates total (global) stats (such as [global count](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats) or [global sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats))
over the specified [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)
and stores these stats in the specified log fields for each input log entry.

The total stats is calculated over the logs sorted by time, so the `<q>` must return the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
in order to properly calculate the total stats.

The `total_stats` pipe puts all the logs returned by `<q>` in memory, so make sure the `<q>` returns the limited number of logs in order to avoid high memory usage.

For example, the following LogsQL query calculates [total sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats) for the `hits` field over the logs for the last 5 minutes:

```logsql
_time:5m | total_stats sum(hits) as total_hits
```

The `| total_stats ...` pipe has the following basic format:

```logsql
... | total_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [total stats function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following total stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` function](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats);
- the sum of `hits` field with the help of [`sum` function](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats):

```logsql
_time:5m
    | total_stats
        count() as total_logs,
        sum(hits) as total_hits
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [total stats function](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `sum(hits)` names for the returned fields:

```logsql
_time:5m | total_stats count(), sum(hits)
```

It is useful to combine `total_stats` with [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets). For example, the following query returns per-hour number of logs over the last day,
plus the total number of logs, and then calculates the per-hour percent of hits over the daily hits.

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

See also:

- [`total_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions)
- [`total_stats` by fields](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-by-fields)
- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

#### total_stats by fields

The following LogsQL syntax can be used for calculating independent total stats per group of log fields:

```logsql
<q> | total_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates total number of logs and total number of `hits` over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m
    | total_stats by (host, path)
        count() total_logs,
        sum(hits) total_hits
```

The `by` keyword can be skipped in `total_stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | total_stats (host, path) count() total_logs, sum(hits) total_hits
```

See also:

- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`total_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions)


