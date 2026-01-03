### split pipe

The `<q> | split <separator> from <src_field> as <dst_field>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) splits `<src_field>` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
obtained from `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `<dst_field>` as a JSON array, by using the given `<separator>`.

For example, the following query splits [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) by `,` and stores the results into `items` field:

```logsql
_time:5m | split "," from _msg as items
```

The `as <dst_field>` part is optional. If it is missing, then the result is stored in the `<src_field>` specified in `from <src_field>`.
For example, the following query stores the split result into `_msg` field:

```logsql
_time:5m | split "," from _msg
```

The `from <src_field>` part is optional. If it is missing, then the `_msg` field is used as a source field. The following query is equivalent to the previous one:

```logsql
_time:5m | split ","
```

It is convenient to use [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) for unrolling the JSON array with the split results.
For example, the following query returns top 5 most frequently seen comma-separated items across [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
for the last 5 minutes:

```logsql
_time:5m | split "," as items | unroll items | top 5 (items)
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`unpack_words` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_words-pipe)


