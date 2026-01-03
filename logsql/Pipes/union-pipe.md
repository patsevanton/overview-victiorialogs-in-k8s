### union pipe

`<q1> | union (<q2>)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns results of `<q1>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) followed by results of `<q2>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).
It works similarly to `UNION ALL` in SQL. `<q1>` and `q2` may contain arbitrary [LogsQL queries](https://docs.victoriametrics.com/victorialogs/logsql/#logsql-tutorial).
For example, the following query returns logs with `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) for the last 5 minutes, plus logs with `panic` word for the last hour:

```logsql
_time:5m error | union (_time:1h panic)
```

See also:

- [`join` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)
- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)

