### replace_regexp pipe

`<q> | replace_regexp ("regexp", "replacement") at field` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) replaces all the substrings matching the given `regexp` with the given `replacement`
in the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) over all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

The `regexp` must contain regular expression with [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
The `replacement` may contain `$N` or `${N}` placeholders, which are substituted with the `N-th` capturing group in the `regexp`.

For example, the following query replaces all the substrings starting with `host-` and ending with `-foo` with the contents between `host-` and `-foo` in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for logs over the last 5 minutes:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1") at _msg
```

The `at _msg` part can be omitted if the replacement occurs in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1")
```

The number of replacements can be limited with `limit N` at the end of `replace_regexp`. For example, the following query replaces only the first `password: ...` substring
ending with whitespace with empty substring at the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `baz`:

```logsql
_time:5m | replace_regexp ('password: [^ ]+', '') at baz limit 1
```

Performance tips:

- It is recommended to use the [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) instead of `replace_regexp` if possible, since it works faster.
- It is recommended to use more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries that are passed to `replace_regexp`.
  See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional replace_regexp](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-replace_regexp)
- [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [`collapse_nums` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`decolorize` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#decolorize-pipe)

#### Conditional replace_regexp

If the [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `replace_regexp`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query replaces `password: ...` substrings ending with whitespace
with `***` in the `foo` field only if the `user_type` field equals `admin`:

```logsql
_time:5m | replace_regexp if (user_type:=admin) ("password: [^ ]+", "***") at foo
```

