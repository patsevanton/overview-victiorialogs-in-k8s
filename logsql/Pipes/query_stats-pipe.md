### query_stats pipe

The `<q> | query_stats` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) returns the following execution statistics for the given [query `<q>`](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax):

- `BytesReadColumnsHeaders` - the number of bytes read from disk for column headers. Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of bytes read for column headers.
- `BytesReadColumnsHeaderIndexes` - the number of bytes read from disk for column header indexes.
- `BytesReadBloomFilters` - the number of bytes read from disk for bloom filters.
- `BytesReadValues` - the number of bytes read from disk for [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
   Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of bytes read for log field values.
- `BytesReadTimestamps` - the number of bytes read from disk for [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field).
- `BytesReadBlockHeaders` - the number of bytes read from disk for block headers.
- `BytesReadTotal` - the total number of bytes read from disk.
- `BlocksProcessed` - the number of data blocks processed during query execution. Use more narrow [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [log stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
  for reducing the number of data blocks processed.
- `RowsProcessed` - the number of log entries processed during query execution. Use more narrow [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [log stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter)
  for reducing the number of processed log entries.
- `RowsFound` - the number of log entries found by the query.
- `ValuesRead` - the number of [log field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) read during query processing.
  Use [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) for reducing the number of field values read.
- `TimestampsRead` - the number of [`_time` fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) read during query processing.
- `BytesProcessedUncompressedValues` - the number of uncompressed bytes for [log field values](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
  which are processed during query execution.
- `QueryDurationNsecs` - the duration of the query in nanoseconds. It can be used for calculating various rates over the query stats with the [`math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

This pipe is useful for investigation and optimizing slow queries.

See also:

- [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe)
- [query troubleshooting](https://docs.victoriametrics.com/victorialogs/logsql/#troubleshooting)

