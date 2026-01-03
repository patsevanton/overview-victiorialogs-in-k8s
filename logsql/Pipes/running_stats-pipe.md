## Конвейер `running_stats`

Конвейер `<q> | running_stats ...` [конвейер](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) вычисляет **накапливаемые статистики** (такие как [накапливаемое количество](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats) или [накапливаемая сумма](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats)) по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), возвращаемым запросом `<q>` [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), и сохраняет эти статистики в указанных полях лога для каждой входной записи.

Накапливаемые статистики вычисляются по логам, отсортированным по времени, поэтому запрос `<q>` **обязан возвращать поле `_time`** [поле времени](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field), чтобы статистика рассчитывалась корректно.

Конвейер `running_stats` загружает в память **все логи**, возвращаемые запросом `<q>`, поэтому убедитесь, что `<q>` возвращает **ограниченное число записей** — это позволит избежать чрезмерного потребления памяти.

**Пример:** следующий запрос LogsQL вычисляет **накапливаемую сумму** для поля `hits` по логам за последние 5 минут:

```logsql
_time:5m | running_stats sum(hits) as running_hits
```

## Базовый формат конвейера `| running_stats ...`

Конвейер `| running_stats ...` имеет следующий базовый формат:

```logsql
... | running_stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Где:
- `stats_func*` — любая из поддерживаемых [функций накапливаемой статистики](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions);
- `result_name*` — имя поля лога, в которое будет сохранён результат соответствующей функции статистики.

Ключевое слово `as` **необязательно**.

**Пример:** следующий запрос вычисляет для логов за последние 5 минут:
- количество записей — с помощью функции [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats);
- сумму поля `hits` — с помощью функции [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats):

```logsql
_time:5m
    | running_stats
        count() as running_logs,
        sum(hits) as running_hits
```

## Опускание имени результата

Можно **не указывать имя результата**. В этом случае имя поля будет совпадать со строковым представлением использованной [функции накапливаемой статистики](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions).

**Пример:** следующий запрос возвращает те же статистики, что и предыдущий, но имена полей будут `count()` и `sum(hits)`:

```logsql
_time:5m | running_stats count(), sum(hits)
```

## Сочетание `running_stats` со статистикой по временным интервалам

Полезно комбинировать `running_stats` со [статистикой по временным интервалам](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets).

**Пример:** следующий запрос возвращает почасовое количество логов за последний день, а также **накапливаемое количество** логов:

```logsql
_time:1d
    | stats by (_time:hour) count() as hits
    | running_stats sum(hits) as running_hits
```

## `running_stats` по полям

Для вычисления **независимых накапливаемых статистик** по группам полей лога используется следующий синтаксис LogsQL:

```logsql
<q> | running_stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Это вычисляет `stats_func*` для каждой группы `(field1, ..., fieldM)` [полей лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), встречающейся в логах, возвращаемых запросом `<q>` [запрос](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

**Пример:** следующий запрос вычисляет накапливаемое количество логов и накапливаемую сумму `hits` за последние 5 минут, с группировкой по полям `(host, path)`:

```logsql
_time:5m
    | running_stats by (host, path)
        count() running_logs,
        sum(hits) running_hits
```

Ключевое слово `by` в конвейере `running_stats ...` можно **опустить**. Например, следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | running_stats (host, path) count() running_logs, sum(hits) running_hits
```
