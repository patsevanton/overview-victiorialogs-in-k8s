### generate_sequence pipe

The `<q> | generate_sequence <N>` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) skips all the `<q>` results and generates `<N>` output logs
with the [`_msg` field](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) containing integer sequence starting from 0 and ending at `N-1`.

This pipe is useful for testing and debugging of the LogsQL pipes. For example, the following query generates 1000 random integers in the range `[0..9]`
and collects the statistics on the number of hits for each random number:

```logsql
* | generate_sequence 1000
    | math round(rand()*10) as rand_num
    | stats by (rand_num) count() hits
    | sort by (rand_num)
```

See also:

- [`rand()` function from `math` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
- [`stats` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)

