### join pipe

The `<q1> | join by (<fields>) (<q2>)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) joins `<q1>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results with the `<q2>` results by the given set of comma-separated `<fields>`.
This pipe works in the following way:

1. It executes the `<q2>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) and remembers its results.
1. For each input row from `<q1>` it searches for matching rows in the `<q2>` results by the given `<fields>`.
1. If the `<q2>` results have no matching rows, then the input row is sent to the output as is.
1. If the `<q2>` results have matching rows, then for each matching row the input row is extended
   with new fields seen at the matching row, and the result is sent to the output.

This logic is similar to `LEFT JOIN` in SQL. For example, the following query returns the number of per-user logs across two applications — `app1` and `app2` (see
[stream filters](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) for details on the `{...}` filter):

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  )
```

If you need results similar to `INNER JOIN` in SQL, then add `inner` suffix after the `join` pipe.
For example, the following query returns stats only for users, which exist in both applications `app1` and `app2`:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) inner
```

It is possible to add a prefix to all the field names returned by the `<query>` by specifying the needed prefix after the `<query>`.
For example, the following query adds `app2.` prefix to all `<query>` log fields:

```logsql
_time:1d {app="app1"} | stats by (user) count() app1_hits
  | join by (user) (
    _time:1d {app="app2"} | stats by (user) count() app2_hits
  ) prefix "app2."
```

**Performance tips**:

- Make sure that the `<query>` in the `join` pipe returns relatively small number of results, since they are kept in RAM during execution of `join` pipe.
- [Conditional `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters) is usually faster to execute.
  They usually require less RAM than the equivalent `join` pipe.

See also:

- [subquery filter](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [conditional `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
- [`filter` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#filter-pipe)

