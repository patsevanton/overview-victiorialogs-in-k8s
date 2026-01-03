### last pipe

`<q> | last N by (fields)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the last `N` logs from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) after sorting them
by the given [`fields`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

For example, the following query returns the last 10 logs with the biggest value of `request_duration` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the last 5 minutes:

```logsql
_time:5m | last 10 by (request_duration)
```

It is possible to return up to `N` logs individually for each group of logs with the same set of [fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
by enumerating the set of these fields in `partition by (...)`.
For example, the following query returns up to 3 logs with the biggest `request_duration` for each host over the last hour:

```logsql
_time:1h | last 3 by (request_duration) partition by (host)
```

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

