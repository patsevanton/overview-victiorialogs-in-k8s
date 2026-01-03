### No-op filter

Sometimes it is needed to apply e.g. `no-op` filter to the given [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
which does nothing, e.g. it matches any logs, even if they do not contain the given log field.

The following options are supported for no-op flter:

- `field_name:in(*)` - a special case for the [`in()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#multi-exact-filter)
- `field_name:contains_any(*)` - a special case for the [`contains_any()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
- `field_name:contains_all(*)` - a special case for the [`contains_all()` filter](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter)

See also:

- [Empty value filter](https://docs.victoriametrics.com/victorialogs/logsql/#empty-value-filter)
- [Any value filter](https://docs.victoriametrics.com/victorialogs/logsql/#any-value-filter)


