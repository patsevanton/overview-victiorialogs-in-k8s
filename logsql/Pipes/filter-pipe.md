### filter pipe

The `<q> | filter ...` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) filters logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) with the given [filter](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

For example, the following query returns `host` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) values
if the number of log messages with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for them over the last hour exceeds `1_000`:

```logsql
_time:1h error | stats by (host) count() logs_count | filter logs_count:> 1_000
```

It is allowed to use `where` prefix instead of `filter` prefix for convenience. For example, the following query is equivalent to the previous one:

```logsql
_time:1h error | stats by (host) count() logs_count | where logs_count:> 1_000
```

It is allowed to omit `filter` prefix if the used filters do not clash with [pipe names](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).
So the following query is equivalent to the previous one:

```logsql
_time:1h error | stats by (host) count() logs_count | logs_count:> 1_000
```

See also:

- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

