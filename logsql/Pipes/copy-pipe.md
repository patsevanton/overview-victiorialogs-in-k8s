### copy pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be copied, then `| copy src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query copies `host` field to `server` for logs over the last 5 minutes, so the output contains both `host` and `server` fields:

```logsql
_time:5m | copy host as server
```

Multiple fields can be copied with a single `| copy ...` pipe. For example, the following query copies
[`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) to `timestamp`, while [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
is copied to `message`:

```logsql
_time:5m | copy _time as timestamp, _msg as message
```

The `as` keyword is optional.

`cp` keyword can be used instead of `copy` for convenience. For example, `_time:5m | cp foo bar` is equivalent to `_time:5m | copy foo as bar`.

It is possible to copy multiple fields with identical prefix to fields with another prefix. For example, the following query copies
all the fields with the prefix `foo` to fields with the prefix `bar`:

```logsql
_time:5m | copy foo* as bar*
```

See also:

- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

