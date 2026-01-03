## Query options

VictoriaLogs supports the following options, which can be passed in the beginning of [LogsQL query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>`
via `options(opt1=v1, ..., optN=vN) <q>` syntax:

### `concurrency` query option

VictoriaLogs executes each query on all the available CPU cores in parallel.
This usually provides the best query performance. Sometimes it is needed to reduce the number of used CPU cores,
in order to reduce RAM usage and/or CPU usage.
This can be done by setting `concurrency` option to the value smaller than the number of available CPU cores.
For example, the following query executes on at most 2 CPU cores:

```logsql
options(concurrency=2) _time:1d | count_uniq(user_id)
```

The `concurrency` option is applied individually to every `vlstorage` node in [VictoriaLogs cluster](https://docs.victoriametrics.com/victorialogs/cluster/).

See also [`parallel_readers` query option](https://docs.victoriametrics.com/victorialogs/logsql/#parallel_readers-query-option).

### `parallel_readers` query option

VictoriaLogs uses parallel data readers for query execution. The default number of parallel readers fits the majority of practical use cases.
Sometimes it may be needed to configure it on a per-query basis (for example, to increase query performance by increasing the number of parallel readers
when the logs are stored on the persistent storage with high read latency such as NFS or S3).
This can be done via `parallel_readers` query option. For example, the following query uses 100 parallel readers:

```logsql
options(parallel_readers=100) _time:1d error | count()
```

If the `parallel_readers` option isn't set, while the [`concurrency` option](https://docs.victoriametrics.com/victorialogs/logsql/#concurrency-query-option) is set,
then the number of parallel readers equals the `concurrency`.

The default number of parallel readers can be configured via `-defaultParallelReaders` command-line flag.

The `parallel_readers` option is applied individually to every `vlstorage` node in [VictoriaLogs cluster](https://docs.victoriametrics.com/victorialogs/cluster/).

Note that too large a number of parallel readers may result in excessive usage of RAM and CPU.

### `ignore_global_time_filter` query option

When running via Web UI, Grafana, or APIs that may apply a global time range, VictoriaLogs injects a global `_time:[start,end]` filter into the query. Set `ignore_global_time_filter=true` to prevent injecting this global time filter.

For example, the following query preserves the original time logic in the query body without adding a global `_time` filter:

```logsql
options(ignore_global_time_filter=true) _time:>1h | count()
```

### `allow_partial_response` query option

In VictoriaLogs cluster mode, some `vlstorage` nodes may be temporarily unavailable. Set `allow_partial_response=true` to return partial results from available nodes instead of failing the whole query.

For example:

```logsql
options(allow_partial_response=true) _time:1h error | stats count()
```

This may lead to incorrect results, so be careful when using this option. However, it's better to use this option instead of setting the `-search.allowPartialResponse` flag for more explicit control.

### `time_offset` query option

`time_offset` query option subtracts the given offset from all the [time filters](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) in the query,
and then adds the given offset to the selected [`_time` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) values
before passing them to query [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes). Allows comparing query results for the same duration at different offsets.
Accepts [duration values](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values) like `12h`, `1d`, `1y`.
For example, the following query returns the number of logs with the `error` [word](https://docs.victoriametrics.com/victorialogs/logsql/#word)
over the last hour 7 days ago.

```logsql
options(time_offset=7d) _time:1h error | stats count() as 'errors_7d_ago'
```

### `ignore_global_time_filter` query option

`ignore_global_time_filter` query option allows ignoring time filter from `start` and `end` args of [HTTP querying API](https://docs.victoriametrics.com/victorialogs/querying/#http-api)
for the given (sub)query. For example, the following query returns the number of logs with `user_id` values seen in logs during December 2024, on the `[start...end)`
time range passed to [`/select/logsql/query`](https://docs.victoriametrics.com/victorialogs/querying/#querying-logs):

```logsql
user_id:in(options(ignore_global_time_filter=true) _time:2024-12Z | keep user_id) | count()
```

The `in(...)` [subquery](https://docs.victoriametrics.com/victorialogs/logsql/#subquery-filter) without `options(ignore_global_time_filter=true)`
takes into account only `user_id` values on the intersection of December 2024 and `[start...end)` time range passed
to [`/select/logsql/query`](https://docs.victoriametrics.com/victorialogs/querying/#querying-logs):

```logsql
user_id:in(_time:2024-12Z | keep user_id) | count()
```

### `allow_partial_response` query option

`allow_partial_response` query option can be used in [VictoriaLogs cluster setup](https://docs.victoriametrics.com/victorialogs/cluster/)
for allowing partial responses when some of `vlstorage` nodes are unavailable for querying. For example, the following query returns
logs for the last 5 minutes when some of the `vlstorage` nodes are unavailable (so the response may miss some logs, which are stored on the unavailable `vlstorage` nodes):

```logsql
options(allow_partial_response=true) _time:5m
```

See also [partial response docs](https://docs.victoriametrics.com/victorialogs/querying/#partial-responses).

