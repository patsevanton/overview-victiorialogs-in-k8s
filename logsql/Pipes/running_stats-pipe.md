### running_stats pipe

The `<q> | running_stats ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) calculates running stats (such as [running count](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats) or [running sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats))
over the specified [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)
and stores the stats in the specified log fields for each input log entry.

The running stats is calculated over the logs sorted by time, so the `<q>` must return the [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field)
in order to properly calculate the running stats.

The `running_stats` pipe puts all the logs returned by `<q>` in memory, so make sure the `<q>` returns the limited number of logs in order to avoid high memory usage.

For example, the following LogsQL query calculates [running sum](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats) for the `hits` field over the logs for the last 5 minutes:

```logsql
_time:5m | running_stats sum(hits) as running_hits
```

The `| running_stats ...` pipe has the following basic format:

```logsql
... | running_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Where `stats_func*` is any of the supported [running stats function](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions), while the `result_name*` is the name of the log field
to store the result of the corresponding stats function. The `as` keyword is optional.

For example, the following query calculates the following running stats for logs over the last 5 minutes:

- the number of logs with the help of [`count` function](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats);
- the sum of `hits` field with the help of [`sum` function](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats):

```logsql
_time:5m
    | running_stats
        count() as running_logs,
        sum(hits) as running_hits
```

It is allowed omitting the result name. In this case the result name equals the string representation of the used [running stats function](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions).
For example, the following query returns the same stats as the previous one, but gives `count()` and `sum(hits)` names for the returned fields:

```logsql
_time:5m | running_stats count(), sum(hits)
```

It is useful to combine `running_stats` with [stats by time buckets](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets). For example, the following query returns per-hour number of logs over the last day,
plus running number of logs.

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | running_stats sum(hits) as running_hits
```

See also:

- [`running_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions)
- [`running_stats` by fields](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-by-fields)
- [`total_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

#### running_stats by fields

The following LogsQL syntax can be used for calculating independent running stats per group of log fields:

```logsql
<q> | running_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

This calculates `stats_func*` for each `(field1, ..., fieldM)` group of [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
seen in the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query calculates running number of logs and running number of `hits` over the last 5 minutes,
grouped by `(host, path)` fields:

```logsql
_time:5m
    | running_stats by (host, path)
        count() running_logs,
        sum(hits) running_hits
```

The `by` keyword can be skipped in `running_stats ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | running_stats (host, path) count() running_logs, sum(hits) running_hits
```

See also:

- [`running_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
- [`running_stats` pipe functions](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions)


