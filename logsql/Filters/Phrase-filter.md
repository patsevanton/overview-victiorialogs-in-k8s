### Phrase filter

If you need to search for log messages with the specific phrase inside them, then just wrap the phrase into quotes according to [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#string-literals).
The phrase can contain any chars, including whitespace, punctuation, parens, etc. They are taken into account during the search.
For example, the following query matches [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
with `ssh: login fail` phrase inside them:

```logsql
"ssh: login fail"
```

This query matches the following [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

- `ERROR: ssh: login fail for user "foobar"`
- `ssh: login fail!`

This query doesn't match the following log messages:

- `ssh login fail`, since the message misses `:` char just after the `ssh`.
  Use `seq("ssh", "login", "fail")` query if log messages with the sequence of these words must be found. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#sequence-filter) for details.
- `login fail: ssh error`, since the message doesn't contain the full phrase requested in the query. If you need matching a message
  with all the [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) listed in the query, then use `ssh AND login AND fail` query. See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter) for details.
- `ssh: login failed`, since the message ends with `failed` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word) instead of `fail` word. Use `"ssh: login fail"*` query for this case.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter) for details.
- `SSH: login fail`, since the `SSH` word is in capital letters. Use `i("ssh: login fail")` for case-insensitive search.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter) for details.

If the phrase contains double quotes, then either put `\` in front of double quotes or put the phrase inside single quotes. For example, the following filter searches
logs with `"foo":"bar"` phrase:

```logsql
'"foo":"bar"'
```

By default the given phrase is searched in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Specify the [field name](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) in front of the phrase and put a colon after it
if it must be searched in the given field. For example, the following query returns log entries containing the `cannot open file` phrase in the `event.original` field:

```logsql
event.original:"cannot open file"
```

Both the field name and the phrase can contain arbitrary [utf-8](https://en.wikipedia.org/wiki/UTF-8)-encoded chars. For example:

```logsql
შეტყობინება:"Το αρχείο δεν μπορεί να ανοίξει"
```

The field name can be put inside quotes if it contains special chars, which may clash with the query syntax.
For example, the following query searches for the `cannot open file` phrase in the field `some:message`:

```logsql
"some:message":"cannot open file"
```

See also:

- [Exact filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Substring filter](https://docs.victoriametrics.com/victorialogs/logsql/#substring-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

