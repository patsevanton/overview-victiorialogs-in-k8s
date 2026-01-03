## Troubleshooting

LogsQL works well for most use cases when set up right. But sometimes you will see slow queries. The most common reason is querying too many logs without enough filtering.
Always **be specific** when you build your queries.

Use these steps to help you understand your query and improve its speed.

### Check how many logs your query matches

You can do this by putting the [`| count()`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) after every filter or pipe that might change the number of rows.

Suppose you have the following query, which executes slowly:

```logsql
_time:5m host:"api-" level:error "database" | stats by (app) count()
```

Substitute all the [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) in the query with `| count()` and
run the updated query to see the total number of matching logs:

```logsql
_time:5m host:"api-" level:error "database" | count()
```

An example output (obtained via [vlogscli](https://docs.victoriametrics.com/victorialogs/querying/vlogscli/), but you can use
[any supported querying method](https://docs.victoriametrics.com/victorialogs/querying/)):

```bash
executing [_time:5m level:error database host:"api-" | stats count(*) as "count(*)"]...; duration: 0.474s
{
  "count(*)": "19217008"
}
```

So the given filters match 19,217,008 logs and the matching takes 0.474 seconds.

If the execution time is high, try reordering your filters. Put the most selective and cheapest conditions first.
Filters run one after another, so an early filter that removes a lot of logs will make later filters faster to run.
For more tips, see the [Performance Tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

If you are not sure which filter is the most selective or the most expensive, you can add `| count()` after each filter while removing the rest of filters.
This helps you see how many logs each filter matches and gives you an idea about their performance:

```logsql
_time:5m level:error | count()
```

```logsql
_time:5m host:"api-" | count()
```

```logsql
_time:5m "database" | count()
```

The [`_time` filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) is the essential one - if it is missing, then VictoriaLogs literally scans all the logs stored in the database.
The `_time` filter allows reducing the amount of logs to scan to the given time range only. Note that [Web UI for VictoriaLogs](https://docs.victoriametrics.com/victorialogs/querying/#web-ui)
and [Grafana plugin for VictoriaLogs](https://docs.victoriametrics.com/victorialogs/integrations/grafana/) automatically set the `_time` filter to the selected time range,
so there is no need to specify it manually in the query.

### Test stream filters in the query

If the query doesn't contain [log stream filters](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter), VictoriaLogs needs to read and scan all the data blocks on the selected time range.
If you add a [log stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter), like this:

```logsql
{app="nginx"}
```

Then VictoriaLogs skips all the data blocks that do not match this stream filter. This is much faster. So, having a good log stream filter is important for query performance.

However, if your [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) has a stream field like `app="nginx"` but you write your filter as:

```logsql
app:=nginx
```

Then VictoriaLogs treats it as a regular ["exact match" filter](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter) and scans all the data blocks, so it will not be as fast as the corresponding stream filter.
Make sure to use the correct stream filter syntax. See [stream filters docs](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) for details.

### Check the number of unique log streams

Log stream filters can help improve query performance, but they are not a magic fix for everything. Watch out for the following common problems:

- If you have too many log streams, and each stream only covers a few logs, query performance can drop significantly.
- If the log stream you are searching in covers a large number of logs (e.g., hundreds of millions and more), searching in that stream can be slow.

To check the number of log streams on the given time range, keep only the time filter and add `| count_uniq(_stream_id)` at the end of the query (see [`count_uniq` docs](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)).
For example, to see how many log streams you have in the last day:

```logsql
_time:1d | count_uniq(_stream_id)
```

The result could be:

```
{
  "count_uniq(_stream_id)": "954"
}
```

This means that the logs over the last day contain 954 unique log streams.

The following query returns top 10 log streams with the biggest number of log entries (it uses [`top` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)):

```logsql
_time:1d | top 10 by (_stream)
```

The following query returns the number of unique log streams and the number of logs for the `{app="nginx"}` [stream filter](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter) over the last day:

```logsql
_time:1d {app="nginx"}
  | stats
      count_uniq(_stream) as streams,
      count() as logs
```

It uses [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe).

Streams with small number of logs usually happen when one or more stream fields have too many different values.
In these cases it is better to remove those fields from the set of log stream fields - see [these docs](https://docs.victoriametrics.com/victorialogs/keyconcepts/#high-cardinality).

### Identify the most costly parts of the query

To see which parts of your logs take up the most space or slow down searches, you can use the [`block_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe).
It returns detailed per-block statistics for your data.

Start with your usual query. Then add the pipe `| keep <field list> | block_stats`:

```logsql
_time:1d | keep kubernetes.pod_name, kubernetes.pod_namespace | block_stats
```

The [`keep` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) keeps only the enumerated log fields and removes the others, so you get statistics just for the fields you care about.
Include every field that appears in [filters](https://docs.victoriametrics.com/victorialogs/logsql/#filters) or [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) of the analyzed query.

Sometimes, the raw numbers returned by `stats` pipe are still too detailed to be useful. You can add the [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) to summarize the numbers:

```logsql
_time:1d
  | keep kubernetes.pod_name, kubernetes.pod_namespace
  | block_stats
  | stats by (field)
      sum(values_bytes)  values_bytes_on_disk,
      sum(rows)          rows
  | sort by (values_bytes_on_disk) desc
```

Example output:

```
values_bytes_on_disk: 561  field: kubernetes.pod_name       rows: 172
values_bytes_on_disk: 101  field: kubernetes.pod_namespace  rows: 172
```

Summing up value bytes and rows lets you see, at a glance, which fields occupy the most disk space or force VictoriaLogs to scan more data.

When you know which fields are expensive, you can decide whether to drop the noisy field from the query, split it out, or change your filters to avoid reading extra data.

You can find more details here: [How to determine which log fields occupy the most of disk space?](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-fields-occupy-the-most-of-disk-space).

It might be useful to add the [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe) to the end of the query in order to understand how much data of different types the query reads and processes.

### Profile pipes incrementally

Suppose you need to profile and optimize the following query:

```logsql
_time:5m -"cannot open file" error
  | extract "user_id=(<uid>)"
  | top 5 by (uid)
```

Drop all the [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) from the query and leave only
the [time range filter](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) like `_time:5m`.
This query returns all the logs on the given time range. If the query is executed
via [the built-in web UI](https://docs.victoriametrics.com/victorialogs/querying/#web-ui) or
via [the Grafana plugin for VictoriaLogs](https://docs.victoriametrics.com/victorialogs/integrations/grafana/),
then just leave `*` in the query input field, since both the web UI and Grafana plugin for VictoriaLogs automatically filter
logs on the selected time range. Add [`| count()`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) at the end of the query and measure the time it takes to execute.
This is the worst-case time needed for executing the query. The query also returns the number of logs, which need to be processed
in the worst case during query execution:

```logsql
_time:5m | count()
```

Then add filters from the original query one by one and measure the resulting query performance. Try different filters from the original
query, leaving the filter that executes faster for each step.

```logsql
_time:5m error | count()
```

```logsql
_time:5m error -"cannot open file" | count()
```

If you hit some slow filter, try replacing it with faster and more specific filter.
See [the performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips) for details.
For example, the slow `-"cannot open file"` filter can be replaced with the faster [`contains_any(phrase1, ..., phraseN)`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter)
filter where `phrase1`, ..., `phraseN` are phrases seen in the logs you want to select:

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") | count()
```

After all the needed filters are added to the query, look at the number of matching logs.
If the number is too big (e.g. exceeds tens of millions), then, probably, more specific
filters can be added to the query in order to reduce the number of logs to process
by the [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).
For example, adding [phrase filters](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter) on constant string parts
from the [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe) pattern can significantly reduce the number of logs
to process by the `extract` pipe:

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") "user_id=(" | count()
```

Then add pipes from the original query one by one and measure the query duration for each step:

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") "user_id=("
  | extract "user_id=(<uid>)"
  | count()
```

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") "user_id=("
  | extract "user_id=(<uid>)"
  | top 5 by (uid)
  | count()
```

If the query becomes slow or starts using a lot of RAM after adding the next filter or pipe, you will know exactly which part of the query to fix.

It might be useful to add the [`query_stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe) to the end of the query in order to understand how much data of different types the query reads and processes.

If you find a slow filter or pipe, try these ideas:

- Regex matching and JSON parsing are expensive. Use faster alternatives if you can. See [performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).
- Sorting without a limit with [`sort` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) stores all logs in memory. Add a `limit` or reduce the input number of logs.
- High-cardinality functions like [`count_uniq()`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats) track every unique value in memory. Think how to reduce the number of unique values to track.
- Large group counts in [`stats by (...)`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields) can use a lot of memory. Filter or transform your data to reduce the number of groups.
