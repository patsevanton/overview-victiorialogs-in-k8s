### Exact prefix filter

Sometimes it is needed to find log messages starting with some prefix. This can be done with the `="prefix"*` filter.
For example, the following query matches log messages, which start from `Processing request` prefix:

```logsql
="Processing request"*
```

This filter matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `Processing request foobar`
- `Processing requests from ...`

It doesn't match the following log messages:

- `processing request foobar`, since the log message starts with lowercase `p`. Use `="processing request"* OR ="Processing request"*`
  query in this case. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `start: Processing request`, since the log message doesn't start with `Processing request`. Use `"Processing request"` query in this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) for details.

By default the `exact` filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the `exact` filter and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries with `log.level` field, which starts with `err` prefix:

```logsql
log.level:="err"*
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
log.დონე:="შეცდომა"*
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query matches `log:level` values starting with `err` prefix:

```logsql
"log:level":="err"*
```

See also:

- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

