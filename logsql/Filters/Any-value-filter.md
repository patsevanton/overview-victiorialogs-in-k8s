### Any value filter

Sometimes it is needed to find log entries containing any non-empty value for the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
This can be performed with `log_field:*` syntax. For example, the following query matches log entries with non-empty `host.hostname` field:

```logsql
host.hostname:*
```

See also:

- [No-op filter](https://docs.victoriametrics.com/victorialogs/logsql/#no-op-filter)
- [Empty value filter](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter)
- [Prefix filter](https://docs.victoriametrics.com/victorialogs/logsql/#prefix-filter)
- [Logical filter](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)

