### Труба `offset` (пропуск записей)

Если после применения трубы [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe) требуется пропустить некоторое количество отобранных записей, можно использовать трубу `| offset N`, где `N` — любое [поддерживаемое целочисленное значение](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).

Например, следующий запрос пропускает первые 100 записей за последние 5 минут после их сортировки по полю [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field):

```logsql
_time:5m | sort by (_time) | offset 100
```

Для удобства вместо ключевого слова `offset` можно использовать `skip`. Например, `_time:5m | skip 10` эквивалентно `_time:5m | offset 10`.

**Важно:** пропуск строк без предварительной сортировки малополезен, поскольку из соображений производительности они могут возвращаться в произвольном порядке. Для сортировки строк используйте трубу [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).

См. также:

- труба [`limit`](https://docs.victoriametrics.com/victorialogs/logsql/#limit-pipe);
- труба [`sort`](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe).
