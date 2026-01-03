### Word filter

The simplest LogsQL query consists of a single [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) to search in log messages. For example, the following query matches
[log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) with `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) inside them:

```logsql
error
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `error`
- `an error happened`
- `error: cannot open file`

This query doesn't match the following log messages:

- `ERROR`, since the filter is case-sensitive by default. Use `i(error)` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.
- `multiple errors occurred`, since the `errors` word doesn't match `error` word. Use `error*` for this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) for details.

By default the given [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) is searched in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the word and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries containing the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) in the `log.level` field:

```logsql
log.level:error
```

Both the field name and the word in the query can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
სფერო:τιμή
```

Both the field name and the word in the query can be put inside quotes if they contain special chars, which may clash with the query syntax.
For example, the following query searches for the ip `1.2.3.45` in the field `ip:remote`:

```logsql
"ip:remote":"1.2.3.45"
```

See also:

- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

