### sort pipe

By default logs are selected in arbitrary order for performance reasons. If logs must be sorted, then `<q> | sort by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used
for sorting logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) by the given [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
using [natural sorting](https://en.wikipedia.org/wiki/Natural_sort_order).

For example, the following query returns logs for the last 5 minutes sorted by [`_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
and then by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | sort by (_stream, _time)
```

Add `desc` after the given log field in order to sort in reverse order of this field. For example, the following query sorts logs in reverse order of `request_duration_seconds` field:

```logsql
_time:5m | sort by (request_duration_seconds desc)
```

The reverse order can be applied globally via `desc` keyword after `by(...)` clause:

```logsql
_time:5m | sort by (foo, bar) desc
```

The `by` keyword can be skipped in `sort ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | sort (foo, bar) desc
```

The `order` alias can be used instead of `sort`, so the following query is equivalent to the previous one:

```logsql
_time:5m | order by (foo, bar) desc
```

Sorting a large number of logs can consume a lot of CPU time and memory. Sometimes it is enough to return the first `N` entries with the biggest
or the smallest values. This can be done by adding `limit N` to the end of `sort ...` pipe.
Such a query consumes less memory when sorting a large number of logs, since it keeps in memory only `N` log entries.
For example, the following query returns top 10 log entries with the biggest values
for the `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) during the last hour:

```logsql
_time:1h | sort by (request_duration desc) limit 10
```

This query is equivalent to the following one, which uses [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe):

```logsql
_time:1h | last 10 by (request_duration)
```

If the first `N` sorted results must be skipped, then `offset N` can be added to `sort` pipe. For example,
the following query skips the first 10 logs with the biggest `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
and then returns the next 20 sorted logs for the last 5 minutes:

```logsql
_time:1h | sort by (request_duration desc) offset 10 limit 20
```

It is possible to sort the logs and apply the `limit` individually for each group of logs with the same set of [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
by enumerating the set of these fields in `partition by (...)`.
For example, the following query returns up to 3 logs with the biggest `request_duration` for each host over the last hour:

```logsql
_time:1h | sort by (request_duration desc) partition by (host) limit 3
```

It is possible to return a rank (sort order number) for every sorted log by adding `rank as <fieldName>` to the end of the `| sort ...` pipe.
For example, the following query stores rank for sorted by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) logs
into `position` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:5m | sort by (_time) rank as position
```

Note that sorting a large number of logs can be slow and can consume a lot of additional memory.
It is recommended to limit the number of logs before sorting with the following approaches:

- Adding `limit N` to the end of `sort ...` pipe.
- Reducing the selected time range with [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter).
- Using more specific [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters), so they select less logs.
- Limiting the number of selected [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) via [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe).

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`offset` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#offset-pipe)

