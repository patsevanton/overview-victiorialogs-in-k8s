### Exact filter

The [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) return [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field),
which contain the given word or phrase inside them. The message may contain additional text other than the requested word or phrase. If you need to search for log messages
or [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) with the exact value, then use the `exact` filter.
For example, the following query returns log messages with the exact value `fatal error: cannot find /foo/bar`:

```logsql
="fatal error: cannot find /foo/bar"
```

The query doesn't match the following log messages:

- `fatal error: cannot find /foo/bar/baz` or `some-text fatal error: cannot find /foo/bar`, since they contain an additional text
  other than the specified in the `exact` filter. Use `"fatal error: cannot find /foo/bar"` query in this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.

- `FATAL ERROR: cannot find /foo/bar`, since the `exact` filter is case-sensitive. Use `i("fatal error: cannot find /foo/bar")` in this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.

By default the `exact` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the `exact` filter and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries with the exact `error` value at `log.level` field:

```logsql
log.level:="error"
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
log.დონე:="შეცდომა"
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query matches the `error` value in the field `log:level`:

```logsql
"log:level":="error"
```

See also:

- [Field equality filter](https://docs.victoriametrics.com/victorialogs/logsql/#eq_field-filter)
- [Exact prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter)
- [Multi-exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

