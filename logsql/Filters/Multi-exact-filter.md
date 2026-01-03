### Multi-exact filter

Sometimes it is needed to locate log messages with a field containing one of the given values. This can be done with multiple [exact filters](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
combined into a single [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter). For example, the following query matches log messages with `log.level` field
containing either `error` or `fatal` exact values:

```logsql
log.level:(="error" OR ="fatal")
```

While this solution works OK, LogsQL provides simpler and faster solution for this case - the `in()` filter.

```logsql
log.level:in("error", "fatal")
```

It works very fast for long lists passed to `in()`.

There is a special case - `in(*)` - this filter matches all the logs. See [no-op filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter) for details.

It is possible to pass arbitrary [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) inside `in(...)` filter in order to match against the results of this query.
See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) for details.

See also:

- [`contains_any` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

