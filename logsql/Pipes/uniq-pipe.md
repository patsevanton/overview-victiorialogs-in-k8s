### uniq pipe

`<q> | uniq by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns unique values for the given [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax). For example, the following LogsQL query
returns unique values for `ip` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
over logs for the last 5 minutes:

```logsql
_time:5m | uniq by (ip)
```

It is possible to specify multiple fields inside `by(...)` clause. In this case all the unique sets for the given fields
are returned. For example, the following query returns all the unique `(host, path)` pairs for the logs over the last 5 minutes:

```logsql
_time:5m | uniq by (host, path)
```

The unique entries are returned in arbitrary order. Use [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) in order to sort them if needed.

Add `with hits` after `uniq by (...)` in order to return the number of matching logs for each field value:

```logsql
_time:5m | uniq by (host) with hits
```

Unique entries are stored in memory during query execution. Big number of unique selected entries may require a lot of memory.
Sometimes it is enough to return up to `N` unique entries. This can be done by adding `limit N` after `by (...)` clause.
This allows limiting memory usage. For example, the following query returns up to 100 unique `(host, path)` pairs for the logs over the last 5 minutes:

```logsql
_time:5m | uniq by (host, path) limit 100
```

If the `limit` is reached, then arbitrary subset of unique values can be returned. The `hits` calculation doesn't work when the `limit` is reached.

The `by` keyword can be skipped in `uniq ...` pipe. For example, the following query is equivalent to the previous one:

```logsql
_time:5m | uniq (host, path) limit 100
```

See also:

- [`uniq_values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)

