### offset pipe

If some selected logs must be skipped after [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe), then `| offset N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used, where `N` can contain any [supported integer numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).
For example, the following query skips the first 100 logs over the last 5 minutes after sorting them by [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | sort by (_time) | offset 100
```

`skip` keyword can be used instead of `offset` keyword for convenience. For example, `_time:5m | skip 10` is equivalent to `_time:5m | offset 10`.

Note that skipping rows without sorting makes little sense, since they can be returned in arbitrary order for performance reasons.
Rows can be sorted with [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).

See also:

- [`limit` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)

