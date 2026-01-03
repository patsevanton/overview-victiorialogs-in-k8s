### rename pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be renamed, then `| rename src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query renames `host` field to `server` for logs over the last 5 minutes, so the output contains `server` field instead of `host` field:

```logsql
_time:5m | rename host as server
```

Multiple fields can be renamed with a single `| rename ...` pipe. For example, the following query renames `host` to `instance` and `app` to `job`:

```logsql
_time:5m | rename host as instance, app as job
```

The `as` keyword is optional.

`mv` keyword can be used instead of `rename` keyword for convenience. For example, `_time:5m | mv foo bar` is equivalent to `_time:5m | rename foo as bar`.

It is possible to rename multiple fields with the given prefix to fields with another prefix. For example, the following query renames all the fields
starting with `foo` prefix to fields starting with `bar` prefix:

```logsql
_time:5m | rename foo* as bar*
```

It is also possible to remove the common prefix from some fields. For example, the following query removes the `foo` prefix from all the fields that start with `foo`:

```logsql
_time:5m | rename foo* as *
```

It is also possible to add a common prefix to all the fields. For example, the following query adds the `foo` prefix to all the fields:

```logsql
_time:5m | rename * as foo*
```

See also:

- [`copy` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#copy-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)
- [`delete` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#delete-pipe)

