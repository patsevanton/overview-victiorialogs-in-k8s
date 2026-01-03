## Performance tips

- It is highly recommended to specify a [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) in order to narrow down the search to a specific time range.
- It is highly recommended to specify a [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) in order to narrow down the search
  to specific [log streams](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields).
- It is recommended to specify the [log fields](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) you need in query results
  with the [`fields` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe), if the selected log entries contain a large number of fields that aren't interesting to you.
  This saves disk read IO and CPU time needed for reading and unpacking all the log fields from disk.
- Move faster filters such as [word filter](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) and [phrase filter](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
  to the beginning of the query.
  This rule doesn't apply to [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter),
  which can be put at any place of the query.
- Move more specific filters, which match lower number of log entries, to the beginning of the query.
  This rule doesn't apply to [time filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) and [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter),
  which can be put at any place of the query.
- If the selected logs are passed to [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) for further transformations and statistics calculations, then it is recommended
  reducing the number of selected logs by using more specific [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters),
  which return lower number of logs to process by [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).
- If the logs are stored at high-latency storage systems such as NFS or S3, then increasing the number of parallel readers can help improve query performance.
  See [these docs](https://docs.victoriametrics.com/victorialogs/logsql/#parallel_readers-query-option) for details.

See also [query performance troubleshooting](https://docs.victoriametrics.com/victorialogs/logsql/#troubleshooting).

