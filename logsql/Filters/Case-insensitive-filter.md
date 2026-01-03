### Case-insensitive filter

Case-insensitive filter can be applied to any word, phrase or prefix by wrapping the corresponding [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter),
[phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) or [prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) into `i()`. For example, the following query returns
log messages with `error` word in any case:

```logsql
i(error)
```

The query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `unknown error happened`
- `ERROR: cannot read file`
- `Error: unknown arg`
- `An ErRoR occurred`

The query doesn't match the following log messages:

- `FooError`, since the `FooError` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) has superfluous prefix `Foo`. Use `~"(?i)error"` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) for details.
- `too many Errors`, since the `Errors` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) has superfluous suffix `s`. Use `i(error*)` for this case.

By default the `i()` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `log.level` field containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in any case:

```logsql
log.level:i(error)
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `log:level` field containing `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in any case.

```logsql
"log:level":i("error")
```

Performance tips:

- Prefer using [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter) over `i(...)`,
  since `contains_common_case(...)` usually works much faster.
- Prefer using case-sensitive filters such as [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
  and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) over case-insensitive filter.
- Prefer moving [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter), [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
  and [prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) in front of the case-insensitive filter
  when using [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [`contains_common_case` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_common_case-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

