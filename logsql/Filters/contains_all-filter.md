### contains_all filter

If it is needed to find logs, which contain all the given [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases, then `v1 AND v2 ... AND vN` [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
can be used. VictoriaLogs provides an alternative approach with the `contains_all(v1, v2, ..., vN)` filter. For example, the following query matches logs,
which contain both `foo` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) and `"bar baz"` phrase in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_all(foo, "bar baz")
```

This is equivalent to the following query:

```logsql
foo AND "bar baz"
```

There is a special case - `contains_all(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `contains_all(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [`seq` filter](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter)
- [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)

