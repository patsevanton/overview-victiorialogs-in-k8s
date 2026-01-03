### Пайп `stats`

Пайп `<q> | stats ...` вычисляет различные статистики по логам, возвращаемым запросом `<q>` ([синтаксис запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax)).

Например, следующий запрос LogsQL использует функцию статистики [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) для подсчёта количества логов за последние 5 минут:

```logsql
_time:5m | stats count() as logs_total
```

Пайп `| stats ...` имеет следующий базовый формат:

```logsql
... | stats
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Где `stats_func*` — любая из поддерживаемых [функций статистики](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions), а `result_name*` — имя поля лога, в которое будет записан результат соответствующей функции. Ключевое слово `as` является необязательным.

Например, следующий запрос вычисляет следующие статистики по логам за последние 5 минут:

* количество логов с помощью функции [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats);
* количество уникальных [потоков логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) с помощью функции [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats):

```logsql
_time:5m | stats count() logs_total, count_uniq(_stream) streams_total
```

Для удобства допускается опускать префикс `stats`. Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | count() logs_total, count_uniq(_stream) streams_total
```

Также допускается опускать имя результата. В этом случае имя результата будет равно строковому представлению используемой функции статистики. Например, следующий запрос возвращает те же статистики, что и предыдущий, но использует имена `count()` и `count_uniq(_stream)` для возвращаемых полей:

```logsql
_time:5m | count(), count_uniq(_stream)
```

См. также:

* [функции пайпа `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
* [статистика по полям](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields)
* [статистика по временным бакетам](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets)
* [статистика по временным бакетам с учётом смещения часового пояса](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-time-buckets-with-timezone-offset)
* [статистика по бакетам полей](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-field-buckets)
* [статистика по IPv4-бакетам](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-ipv4-buckets)
* [статистика с дополнительными фильтрами](https://docs.victoriametrics.com/victorialogs/logsql/#stats-with-additional-filters)
* [`running_stats` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe)
* [`total_stats` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe)
* [`math` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe)
* [`sort` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#sort-pipe)
* [`uniq` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#uniq-pipe)
* [`top` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)
* [`join` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)



### Статистика по полям

Следующий синтаксис LogsQL может использоваться для вычисления независимых статистик по группам полей логов:

```logsql
<q> | stats by (field1, ..., fieldM)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Это вычисляет `stats_func*` для каждой группы `(field1, ..., fieldM)` [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), встречающихся в логах, возвращаемых запросом `<q>`.

Например, следующий запрос вычисляет количество логов и количество уникальных IP-адресов за последние 5 минут, сгруппированных по полям `(host, path)`:

```logsql
_time:5m | stats by (host, path) count() logs_total, count_uniq(ip) ips_total
```

Ключевое слово `by` может быть опущено в пайпе `stats`. Например, следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | stats (host, path) count() logs_total, count_uniq(ip) ips_total
```

См. также:

* [`stats` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
* [функции `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
* [`row_min`](https://docs.victoriametrics.com/victorialogs/logsql/#row_min-stats)
* [`row_max`](https://docs.victoriametrics.com/victorialogs/logsql/#row_max-stats)
* [`row_any`](https://docs.victoriametrics.com/victorialogs/logsql/#row_any-stats)



### Статистика по временным бакетам

Следующий синтаксис может использоваться для вычисления статистики, сгруппированной по временным интервалам:

```logsql
<q> | stats by (_time:step)
  stats_func1(...) as result_name1,
  ...
  stats_funcN(...) as result_nameN
```

Это вычисляет `stats_func*` для каждого шага `step` поля [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) по логам, возвращаемым запросом `<q>`. Значение `step` может быть любым [значением длительности](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values).

Например, следующий запрос возвращает поминутное количество логов и уникальных IP-адресов за последние 5 минут:

```logsql
_time:5m | stats by (_time:1m) count() logs_total, count_uniq(ip) ips_total
```

Часто бывает полезно вычислять накопительные статистики поверх статистик по временным бакетам с помощью пайпа [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe). Например, следующий запрос добавляет накопительное количество логов в поле `running_hits`:

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | running_stats sum(hits) as running_hits
```

Также может быть полезно вычислять итоговые статистики поверх временных бакетов с помощью пайпа [`total_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#total_stats-pipe). Например, следующий запрос добавляет общее количество логов в поле `total_hits`, а затем использует это поле для вычисления поминутного процента запросов с помощью пайпа [`math`](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe):

```logsql
_time:5m
    | stats by (_time:1m) count() as hits
    | total_stats sum(hits) as total_hits
    | math round((hits / total_hits)*100) as hits_percent
```

Дополнительно поддерживаются следующие значения `step`:

* `nanosecond` — равно `1ns`
* `microsecond` — равно `1µs`
* `millisecond` — равно `1ms`
* `second` — равно `1s`
* `minute` — равно `1m`
* `hour` — равно `1h`
* `day` — равно `1d`
* `week` — равно `1w`
* `month` — равно одному месяцу с учётом количества дней
* `year` — равно одному году с учётом количества дней



### Статистика по временным бакетам с учётом часового пояса

VictoriaLogs хранит значения [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) как Unix-время в наносекундах, соответствующее часовому поясу UTC. Иногда требуется вычислять статистику, сгруппированную по дням или неделям в часовом поясе, отличном от UTC. Это возможно с помощью следующего синтаксиса:

```logsql
<q> | stats by (_time:step offset timezone_offset) ...
```

Например, следующий запрос вычисляет количество логов по дням за последнюю неделю в часовом поясе `UTC+02:00`:

```logsql
_time:1w | stats by (_time:1d offset 2h) count() logs_total
```



### Статистика по бакетам полей

Каждое поле лога внутри `<q> | stats by (...)` может быть разбито на бакеты аналогично полю `_time`. В качестве значения `step` может использоваться любое [числовое значение](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).

Например, следующий запрос вычисляет количество запросов за последний час, сгруппированных по 10 КБ поля `request_size_bytes`:

```logsql
_time:1h | stats by (request_size_bytes:10KB) count() requests
```



### Статистика по IPv4-бакетам

Статистика может быть сгруппирована по [полю лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), содержащему IPv4-адреса, с помощью синтаксиса `ip_field_name:/network_mask` внутри `by(...)`.

Например, следующий запрос возвращает количество логов по подсетям `/24`, извлечённым из поля `ip`, за последние 5 минут:

```logsql
_time:5m | stats by (ip:/24) count() requests_per_subnet
```



### Статистика с дополнительными фильтрами

Иногда требуется вычислять статистику по разным подмножествам подходящих логов. Это можно сделать, вставив условие `if (<any_filters>)` между функцией статистики и именем результата. В `any_filters` могут использоваться произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

Например, следующий запрос отдельно вычисляет количество сообщений логов со словами `GET`, `POST` и `PUT`, а также общее количество логов за последние 5 минут:

```logsql
_time:5m | stats
  count() if (GET) gets,
  count() if (POST) posts,
  count() if (PUT) puts,
  count() total
```

Если ни одна входная строка не соответствует фильтру `if (...)`, то для соответствующей функции статистики будет возвращено значение `0`.

См. также:

* [`stats` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe)
* [функции `stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe-functions)
* [`join` пайп](https://docs.victoriametrics.com/victorialogs/logsql/#join-pipe)
