### Prefix filter

If you need to search for log messages with [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrases containing some prefix, then just add `*` char to the end of the [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) / phrase in the query.
For example, the following query returns [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), which contain [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) with `err` prefix:

```logsql
err*
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `err: foobar`
- `cannot open file: error occurred`

This query doesn't match the following log messages:

- `Error: foobar`, since the `Error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) starts with capital letter. Use `i(err*)` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.
- `fooerror`, since the `fooerror` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) doesn't start with `err`. Use `*err*` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter) for details.

Prefix filter can be applied to [phrases](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) put inside quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals). For example, the following query matches
[log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing phrases with `unexpected fail` prefix:

```logsql
"unexpected fail"*
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `unexpected fail: IO error`
- `error:unexpected failure`

This query doesn't match the following log messages:

- `unexpectedly failed`, since the `unexpectedly` doesn't match `unexpected` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word). Use `unexpected* AND fail*` for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `failed to open file: unexpected EOF`, since `failed` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) occurs before the `unexpected` word. Use `unexpected AND fail*` for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.

If the prefix contains double quotes, then either put `\` in front of double quotes or put the prefix inside single quotes. For example, the following filter searches
logs with `"foo":"bar` prefix:

```logsql
'"foo":"bar'*
```

By default the prefix filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the prefix filter
in order to apply it to the given field. For example, the following query matches `log.level` field containing any word with the `err` prefix:

```logsql
log.level:err*
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `log:level` field containing any word with the `err` prefix.

```logsql
"log:level":err*
```

Performance tips:

- Prefer using [word filters](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filters](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) combined via [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
  instead of prefix filter.
- Prefer moving [word filters](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filters](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) in front of prefix filter when using [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Exact prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

