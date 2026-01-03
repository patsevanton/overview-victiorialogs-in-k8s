### contains_any filter

Sometimes it is needed to find logs, which contain at least one [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrase out of many words / phrases.
This can be done with `v1 OR v2 OR ... OR vN` [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
VictoriaLogs provides an alternative approach with the `contains_any(v1, v2, ..., vN)` filter. For example, the following query matches logs,
which contain `foo` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) or `"bar baz"` phrase in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
contains_any(foo, "bar baz")
```

This is equivalent to the following query:

```logsql
foo OR "bar baz"
```

There is a special case - `contains_any(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `contains_any(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [`in` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)

