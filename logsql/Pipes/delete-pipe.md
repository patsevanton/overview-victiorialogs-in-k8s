### delete pipe

If some [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) must be deleted, then `| delete field1, ..., fieldN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used.
For example, the following query deletes `host` and `app` fields from the logs over the last 5 minutes:

```logsql
_time:5m | delete host, app
```

`drop`, `del` and `rm` keywords can be used instead of `delete` for convenience. For example, `_time:5m | drop host` is equivalent to `_time:5m | delete host`.

It is possible to delete fields with common prefix. For example, the following query deletes all the fields with `foo` prefix:

```logsql
_time:5m | delete foo*
```

See also:

- [`rename` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#rename-pipe)
- [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe)

