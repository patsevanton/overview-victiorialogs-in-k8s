### block_stats pipe

`<q> | block_stats` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the following stats for each field in every data block
processed by `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax):

- `field` - [field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) name
- `rows` - the number of rows at the given `field`
- `type` - internal storage type for the given `field`
- `values_bytes` - on-disk size of the data for the given `field`
- `bloom_bytes` - on-disk size of bloom filter data for the given `field`
- `dict_bytes` - on-disk size of the dictionary data for the given `field`
- `dict_items` - the number of unique values in the dictionary for the given `field`
- `_stream` - the [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) for the given `field`
- `part_path` - the path to the data part where the field data is stored

The `block_stats` pipe is needed mostly for debugging purposes.
See, for example, [how to detect which log field occupies the most of the disk space](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-fields-occupy-the-most-of-disk-space),
or [how to detect which log stream occupies the most of the disk space](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-streams-occupy-the-most-of-disk-space).

See also:

- [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
- [`value_type` filter](https://docs.victoriametrics.com/victorialogs/logsql/#value_type-filter)
- [`blocks_count` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#blocks_count-pipe)
- [`len` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#len-pipe)

