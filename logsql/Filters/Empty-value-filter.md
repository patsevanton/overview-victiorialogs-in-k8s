### Empty value filter

Sometimes it is needed to find log entries without the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be performed with `log_field:""` syntax. For example, the following query matches log entries without `host.hostname` field:

```logsql
host.hostname:""
```

See also:

- [No-op filter](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
- [Any value filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter)
- [Word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

