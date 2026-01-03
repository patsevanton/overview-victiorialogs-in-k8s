### replace pipe

`<q> | replace ("old", "new") at field` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) replaces all the occurrences of the `old` substring with the `new` substring
in the given [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) over all the logs returned by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

For example, the following query replaces all the `secret-password` substrings with `***` in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for logs over the last 5 minutes:

```logsql
_time:5m | replace ("secret-password", "***") at _msg
```

The `at _msg` part can be omitted if the replacement occurs in the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
The following query is equivalent to the previous one:

```logsql
_time:5m | replace ("secret-password", "***")
```

The number of replacements can be limited with `limit N` at the end of `replace`. For example, the following query replaces only the first `foo` substring with `bar`
at the [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `baz`:

```logsql
_time:5m | replace ('foo', 'bar') at baz limit 1
```

Performance tip: it is recommended using more specific [log filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) in order to reduce the number of log entries, which are passed to `replace`.
See [general performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.

See also:

- [Conditional replace](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-replace)
- [`replace_regexp` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)
- [`collapse_nums`](https://docs.victoriametrics.com/victorialogs/logsql/#collapse_nums-pipe)
- [`format` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Conditional replace

If the [`replace` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `replace`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query replaces `secret` with `***` in the `password` field
only if the `user_type` field equals `admin`:

```logsql
_time:5m | replace if (user_type:=admin) ("secret", "***") at password
```

