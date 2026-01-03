### Regexp filter

LogsQL supports regular expression filter with [RE2 syntax](https://github.com/google/re2/wiki/Syntax) via `~"regex"` syntax.
The `regex` can be put in one of the supported quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query returns all the log messages containing `err` or `warn` substrings:

```logsql
~"err|warn"
```

The query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), which contain either `err` or `warn` substrings:

- `error: cannot read data`
- `2 warnings have been raised`
- `data transferring finished`

The query doesn't match the following log messages:

- `ERROR: cannot open file`, since the `ERROR` word is in uppercase letters. Use `~"(?i)(err|warn)"` query for case-insensitive regexp search.
  See [these docs](https://github.com/google/re2/wiki/Syntax) for details. See also [case-insensitive filter docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter).
- `it is warmer than usual`, since it doesn't contain neither `err` nor `warn` substrings.

If the regexp contains double quotes, then either put `\` in front of double quotes or put the regexp inside single quotes. For example, the following regexp searches
logs matching `"foo":"(bar|baz)"` regexp:

```logsql
~'"foo":"(bar|baz)"'
```

The `\` char inside the regexp must be encoded as `\\`. For example, the following query searches for logs with `a.b` substring inside them:

```logsql
~"a\\.b"
```

It is recommended to use the [substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter) when a substring search is needed.

By default the regexp filter is applied to the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the needed [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the filter
in order to apply it to the given field. For example, the following query matches `event.original` field containing either `err` or `warn` substrings:

```logsql
event.original:~"err|warn"
```

If the field name contains special chars, which may clash with the query syntax, then it may be put into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
For example, the following query matches `event:original` field containing either `err` or `warn` substrings:

```logsql
"event:original":~"err|warn"
```

Performance tips:

- Prefer combining simple [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) with [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) instead of using regexp filter.
  For example, the `~"error|warning"` query can be substituted with `error OR warning` query, which usually works much faster.
  Note that the `~"error|warning"` matches `errors` as well as `warnings` [words](https://docs.victoriametrics.com/victorialogs/logsql/#word), while `error OR warning` matches
  only the specified [words](https://docs.victoriametrics.com/victorialogs/logsql/#word). See also [multi-exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter).
- Prefer moving the regexp filter to the end of the [logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter), so lighter filters are executed first.
- Prefer using `="some prefix"*` instead of `~"^some prefix"`, since the [`exact prefix` filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-prefix-filter) works much faster than the regexp filter.
- See [other performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

See also:

- [Case-insensitive filter](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

