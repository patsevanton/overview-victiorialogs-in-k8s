### limit pipe

If only a subset of selected logs must be processed, then `| limit N` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used, where `N` can contain any [supported integer numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).
For example, the following query returns up to 100 logs over the last 5 minutes:

```logsql
_time:5m | limit 100
```

`head` keyword can be used instead of `limit` for convenience. For example, `_time:5m | head 100` is equivalent to `_time:5m | limit 100`.

The `N` in `head N` can be omitted - in this case up to 10 matching logs are returned:

```logsql
error | head
```

By default rows are selected in arbitrary order for performance reasons, so the query above can return different sets of logs every time it is executed.
[`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) can be used for making sure the logs are in the same order before applying `limit ...` to them.

See also:

- [`sample` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sample-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`offset` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#offset-pipe)

