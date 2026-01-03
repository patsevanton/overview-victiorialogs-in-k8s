### Sequence filter

Sometimes it is needed to find [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) or phrases in a particular order. For example, if log messages with `error` word followed by `open file` phrase
must be found, then the following LogsQL query can be used (every word / phrase can be quoted according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals)):

```logsql
seq("error", "open file")
```

This query matches `some error: cannot open file /foo/bar` message, since the `open file` phrase goes after the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word).
The query doesn't match the `cannot open file: error` message, since the `open file` phrase is located in front of the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word).
If you need to match log messages with both the `error` word and the `open file` phrase, then use the `error AND "open file"` query. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)
for details.

By default the `seq()` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `event.original` field containing `(error, "open file")` sequence:

```logsql
event.original:seq(error, "open file")
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `event:original` field containing `(error, "open file")` sequence:

```logsql
"event:original":seq(error, "open file")
```

See also:

- [Pattern match filter](https://docs.victoriametrics.com/victorialogs/logsql/#pattern-match-filter)
- [`contains_all` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

