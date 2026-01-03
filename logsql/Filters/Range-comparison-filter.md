### Range comparison filter

LogsQL supports `field:>X`, `field:>=X`, `field:<X` and `field:<=X` filters, where `field` is the name of [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
and `X` is [numeric value](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values), IPv4 address or a string. For example, the following query returns logs containing numeric values for the `response_size` field bigger than `10*1024`:

```logsql
response_size:>10KiB
```

The following query returns logs with `username` field containing string values smaller than `John`:

```logsql
username:<"John"
```

See also:

- [String range filter](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter)
- [Range filter](https://docs.victoriametrics.com/victorialogs/logsql/#range-filter)
- [`le_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#le_field-filter)
- [`lt_field` filter](https://docs.victoriametrics.com/victorialogs/logsql/#lt_field-filter)

