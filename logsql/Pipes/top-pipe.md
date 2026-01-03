### top pipe

`<q> | top N by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns top `N` sets for `(field1, ..., fieldN)` [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
with the maximum number of matching log entries across logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query returns top 7 [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)
with the maximum number of log entries over the last 5 minutes. The number of entries is returned in the `hits` field:

```logsql
_time:5m | top 7 by (_stream)
```

The `N` is optional. If it is skipped, then top 10 entries are returned. For example, the following query returns top 10 values
for `ip` [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) seen in logs for the last 5 minutes:

```logsql
_time:5m | top by (ip)
```

It is possible to give another name for the `hits` field via `hits as <new_name>` syntax. For example, the following query returns top per-`path` hits in the `visits` field:

```logsql
_time:5m | top by (path) hits as visits
```

It is possible to set a `rank` field for each returned entry for the `top` pipe by adding `rank`. For example, the following query sets the `rank` field for each returned `ip`:

```logsql
_time:5m | top 10 by (ip) rank
```

The `rank` field can have other name. For example, the following query uses the `position` field name instead of `rank` field name in the output:

```logsql
_time:5m | top 10 by (ip) rank as position
```

See also:

- [`first` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#first-pipe)
- [`last` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#last-pipe)
- [`facets` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#facets-pipe)
- [`uniq` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
- [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
- [`histogram` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#histogram-stats)

