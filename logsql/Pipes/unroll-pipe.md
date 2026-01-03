### unroll pipe

`<q> | unroll by (field1, ..., fieldN)` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) can be used for unrolling JSON arrays from `field1`, ..., `fieldN`
[log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into separate rows.

For example, the following query unrolls `timestamp` and `value` [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) from logs for the last 5 minutes:

```logsql
_time:5m | unroll (timestamp, value)
```

If the unrolled JSON array contains JSON objects, then it may be handy to use [`unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) for unpacking
the unrolled array items into separate fields for further processing.

See also:

- [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
- [`unpack_words` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)
- [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
- [`uniq_values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#uniq_values-stats)
- [`values` stats function](https://docs.victoriametrics.com/victorialogs/logsql/#values-stats)

#### Conditional unroll

If the [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) must be applied only to some [log entries](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
then add `if (<filters>)` after `unroll`.
The `<filters>` can contain arbitrary [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters). For example, the following query unrolls the `value` field only if the `value_type` field equals `json_array`:

```logsql
_time:5m | unroll if (value_type:="json_array") (value)
```

