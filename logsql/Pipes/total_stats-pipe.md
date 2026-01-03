## Конвейер `total_stats`

Конвейер `<q> | total_stats …` [конвейер](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) вычисляет **общие (глобальные) статистические показатели** (такие как [общее количество](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats) или [общая сумма](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats)) по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), возвращаемым запросом `<q>` [синтаксис запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), и сохраняет эти статистические данные в указанных полях лога для каждой входной записи.

Общая статистика вычисляется по логам, отсортированным по времени, поэтому запрос `<q>` **должен возвращать поле `_time`** [поле времени](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field), чтобы корректно рассчитать общую статистику.

Конвейер `total_stats` загружает в память все логи, возвращённые запросом `<q>`, поэтому убедитесь, что `<q>` возвращает ограниченное число логов — это позволит избежать чрезмерного потребления памяти.

### Пример

Следующий запрос LogsQL вычисляет **общую сумму** для поля `hits` по логам за последние 5 минут:

```logsql
_time:5m | total_stats sum(hits) as total_hits
```

### Базовый формат конвейера `| total_stats …`

```logsql
... | total_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Где:
- `stats_func*` — любая из поддерживаемых [функций общей статистики](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions);
- `result_name*` — имя поля лога, в которое будет сохранён результат соответствующей статистической функции.

Ключевое слово `as` необязательно.

### Пример с несколькими статистиками

Следующий запрос вычисляет за последние 5 минут:
- количество логов — с помощью функции [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-total_stats);
- сумму значений поля `hits` — с помощью функции [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-total_stats):

```logsql
_time:5m
    | total_stats
        count() as total_logs,
        sum(hits) as total_hits
```

Можно **опустить имя результата**. В этом случае имя результата будет равно строковому представлению использованной [функции общей статистики](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe-functions).

Например, следующий запрос возвращает те же статистики, что и предыдущий, но назначает полям имена `count()` и `sum(hits)`:

```logsql
_time:5m | total_stats count(), sum(hits)
```

### Сочетание `total_stats` с группировкой по временным интервалам

Полезно комбинировать `total_stats` с [статистикой по временным интервалам](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets).

Например, следующий запрос возвращает:
- количество логов **по часам** за последние сутки;
- общее количество логов;
- затем вычисляет **процент логов за час** от общего количества за сутки:

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

## `total_stats` по полям

Для вычисления **независимой общей статистики по группам полей лога** используется следующий синтаксис LogsQL:

```logsql
<q> | total_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Это вычисляет `stats_func*` для каждой группы `(field1, ..., fieldM)` [полей лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), встречающихся в логах, возвращённых запросом `<q>` [синтаксис запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

### Пример группировки по полям

Следующий запрос вычисляет за последние 5 минут:
- общее количество логов;
- общую сумму `hits`,

с группировкой по полям `(host, path)`:

```logsql
_time:5m
    | total_stats by (host, path)
        count() total_logs,
        sum(hits) total_hits
```

Ключевое слово `by` в конвейере `total_stats …` можно опустить. Например, следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | total_stats (host, path) count() total_logs, sum(hits) total_hits
```
