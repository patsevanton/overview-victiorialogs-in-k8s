### unpack_words pipe

The `<q> | unpack_words from <src_field> as <dst_field>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) unpacks [words](https://docs.victoriametrics.com/victorialogs/logsql/#word) from the given
`<src_field>` [log field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
of `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) results into `<dst_field>` as a JSON array.

For example, the following query unpacks words from [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) into `words` field:

```logsql
_time:5m | unpack_words from _msg as words
```

The `as <dst_field>` part is optional. If it is missing, then the result is stored in the `<src_field>` specified in `from <src_field>`.
For example, the following query stores the unpacked words into `_msg` field:

```logsql
_time:5m | unpack_words from _msg
```

The `from <src_field>` part is optional. If it is missing, then words are unpacked from the `_msg` field. The following query is equivalent to the previous one:

```logsql
_time:5m | unpack_words
```

By default `unpack_words` pipe unpacks all the words, including duplicates, from the `<src_field>`. It is possible to drop duplicate words by adding `drop_duplicates` suffix to the pipe.
For example, the following query extracts only unique words from every `text` field:

```logsql
_time:5m | unpack_words from text as words drop_duplicates
```

It is convenient to use [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe) for unrolling the JSON array with unpacked words from the destination field.
For example, the following query returns top 5 most frequently seen words across [log messages](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) for the last 5 minutes:

```logsql
_time:5m | unpack_words as words | unroll words | top 5 (words)
```

See also:

- [`unroll` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unroll-pipe)
- [`split` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#split-pipe)

