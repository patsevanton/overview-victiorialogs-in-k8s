Ниже — перевод раздела **Troubleshooting** из документации VictoriaLogs.



## Устранение неполадок (Troubleshooting)

LogsQL хорошо работает в большинстве сценариев при правильной настройке. Однако иногда вы можете сталкиваться с медленными запросами. Самая частая причина — запрос слишком большого количества логов без достаточной фильтрации.
Всегда **будьте максимально конкретны** при построении запросов.

Используйте шаги ниже, чтобы понять, как работает ваш запрос, и повысить его скорость.



### Проверьте, сколько логов соответствует вашему запросу

Это можно сделать, добавляя [`| count()`](https://docs.victoriametrics.com/victorialogs/logsql/#count-stats) после каждого фильтра или pipe, который может менять количество строк.

Предположим, у вас есть следующий запрос, который выполняется медленно:

```logsql
_time:5m host:"api-" level:error "database" | stats by (app) count()
```

Замените все [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) в запросе на `| count()` и выполните обновлённый запрос, чтобы увидеть общее количество совпадающих логов:

```logsql
_time:5m host:"api-" level:error "database" | count()
```

Пример вывода (получен через [vlogscli](https://docs.victoriametrics.com/victorialogs/querying/vlogscli/), но можно использовать
[любой поддерживаемый способ выполнения запросов](https://docs.victoriametrics.com/victorialogs/querying/)):

```bash
executing [_time:5m level:error database host:"api-" | stats count(*) as "count(*)"]...; duration: 0.474s
{
  "count(*)": "19217008"
}
```

Это означает, что указанные фильтры совпадают с 19 217 008 логами, а выполнение заняло 0.474 секунды.

Если время выполнения велико, попробуйте изменить порядок фильтров. Размещайте самые селективные и «дешёвые» условия первыми.
Фильтры выполняются последовательно, поэтому ранний фильтр, который отсекает большое количество логов, ускорит выполнение последующих фильтров.
Дополнительные рекомендации см. в разделе [Performance Tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

Если вы не уверены, какой фильтр наиболее селективный или самый дорогой, можно добавлять `| count()` после каждого фильтра, убирая остальные.
Это позволит увидеть, сколько логов соответствует каждому фильтру, и оценить их производительность:

```logsql
_time:5m level:error | count()
```

```logsql
_time:5m host:"api-" | count()
```

```logsql
_time:5m "database" | count()
```

Фильтр [`_time`](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) является обязательным: если его нет, VictoriaLogs буквально сканирует **все** логи, хранящиеся в базе данных.
Фильтр `_time` позволяет ограничить объём сканируемых данных заданным временным диапазоном.

Обратите внимание: [Web UI VictoriaLogs](https://docs.victoriametrics.com/victorialogs/querying/#web-ui) и
[плагин Grafana для VictoriaLogs](https://docs.victoriametrics.com/victorialogs/integrations/grafana/)
автоматически устанавливают `_time` в соответствии с выбранным временным интервалом, поэтому указывать его вручную не требуется.



### Проверяйте использование stream-фильтров в запросе

Если запрос не содержит [фильтров по потокам логов (log stream filters)](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter), VictoriaLogs вынужден читать и сканировать все блоки данных в выбранном временном диапазоне.

Если же вы добавите stream-фильтр, например:

```logsql
{app="nginx"}
```

то VictoriaLogs пропустит все блоки данных, которые не соответствуют этому фильтру. Это значительно быстрее, поэтому корректные stream-фильтры крайне важны для производительности.

Однако если ваш [log stream](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields) содержит поле `app="nginx"`, а вы напишете фильтр так:

```logsql
app:=nginx
```

VictoriaLogs будет трактовать его как обычный
["точный фильтр совпадения"](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)
и всё равно будет сканировать все блоки данных. Такой запрос будет заметно медленнее, чем аналогичный stream-фильтр.

Убедитесь, что вы используете правильный синтаксис stream-фильтров. Подробности см. в
[документации по stream-фильтрам](https://docs.victoriametrics.com/victorialogs/logsql/#stream-filter).



### Проверьте количество уникальных log stream’ов

Stream-фильтры помогают повысить производительность, но они не являются универсальным решением. Обратите внимание на типичные проблемы:

* Если у вас слишком много log stream’ов, и каждый из них содержит лишь небольшое количество логов, производительность запросов может сильно снизиться.
* Если log stream, в котором вы ищете, содержит очень большое количество логов (например, сотни миллионов и больше), поиск в таком потоке может быть медленным.

Чтобы проверить количество log stream’ов за заданный период, оставьте только фильтр по времени и добавьте `| count_uniq(_stream_id)` в конец запроса
(см. документацию [`count_uniq`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats)).

Например, чтобы узнать, сколько log stream’ов было за последний день:

```logsql
_time:1d | count_uniq(_stream_id)
```

Результат может быть таким:

```
{
  "count_uniq(_stream_id)": "954"
}
```

Это означает, что за последний день логи содержали 954 уникальных log stream’а.

Следующий запрос возвращает топ-10 log stream’ов с наибольшим количеством лог-записей
(используется pipe [`top`](https://docs.victoriametrics.com/victorialogs/logsql/#top-pipe)):

```logsql
_time:1d | top 10 by (_stream)
```

А следующий запрос возвращает количество уникальных log stream’ов и общее число логов
для stream-фильтра `{app="nginx"}` за последний день:

```logsql
_time:1d {app="nginx"}
  | stats
      count_uniq(_stream) as streams,
      count() as logs
```

Здесь используется pipe [`stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe).

Stream’ы с малым числом логов обычно возникают, когда одно или несколько stream-полей имеют слишком много различных значений.
В таких случаях лучше удалить эти поля из набора stream-полей. См. документацию по
[высокой кардинальности](https://docs.victoriametrics.com/victorialogs/keyconcepts/#high-cardinality).



### Определите самые «дорогие» части запроса

Чтобы понять, какие части логов занимают больше всего места или замедляют поиск, можно использовать pipe
[`block_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#block_stats-pipe).
Он возвращает детальную статистику по каждому блоку данных.

Начните с вашего обычного запроса, затем добавьте `| keep <список_полей> | block_stats`:

```logsql
_time:1d | keep kubernetes.pod_name, kubernetes.pod_namespace | block_stats
```

Pipe [`keep`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) оставляет только перечисленные поля логов и удаляет все остальные,
что позволяет получить статистику только по интересующим вас полям.
Включайте все поля, которые используются в [фильтрах](https://docs.victoriametrics.com/victorialogs/logsql/#filters) или
[pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) анализируемого запроса.

Иногда «сырые» данные, возвращаемые `block_stats`, слишком детальны. В этом случае можно добавить pipe
[`stats`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-pipe) для агрегации:

```logsql
_time:1d
  | keep kubernetes.pod_name, kubernetes.pod_namespace
  | block_stats
  | stats by (field)
      sum(values_bytes)  values_bytes_on_disk,
      sum(rows)          rows
  | sort by (values_bytes_on_disk) desc
```

Пример вывода:

```
values_bytes_on_disk: 561  field: kubernetes.pod_name       rows: 172
values_bytes_on_disk: 101  field: kubernetes.pod_namespace  rows: 172
```

Суммирование размера значений и количества строк позволяет быстро увидеть,
какие поля занимают больше всего места на диске или заставляют VictoriaLogs сканировать больше данных.

Поняв, какие поля наиболее «дорогие», вы можете решить:
удалить ли шумное поле из запроса, вынести его отдельно или изменить фильтры, чтобы избежать чтения лишних данных.

Дополнительные детали см. здесь:
[Как определить, какие поля логов занимают больше всего места на диске?](https://docs.victoriametrics.com/victorialogs/faq/#how-to-determine-which-log-fields-occupy-the-most-of-disk-space).

Также может быть полезно добавить pipe
[`query_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
в конец запроса, чтобы понять, сколько данных разных типов читает и обрабатывает запрос.



### Профилируйте pipes поэтапно

Предположим, вам нужно профилировать и оптимизировать следующий запрос:

```logsql
_time:5m -"cannot open file" error
  | extract "user_id=(<uid>)"
  | top 5 by (uid)
```

Удалите все [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) и оставьте только
[фильтр по времени](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter), например `_time:5m`.

Если запрос выполняется через
[встроенный Web UI](https://docs.victoriametrics.com/victorialogs/querying/#web-ui)
или через
[плагин Grafana для VictoriaLogs](https://docs.victoriametrics.com/victorialogs/integrations/grafana/),
достаточно оставить `*` в поле запроса, так как временной диапазон будет применён автоматически.

Добавьте `| count()` и измерьте время выполнения — это худший возможный сценарий по времени и объёму данных:

```logsql
_time:5m | count()
```

Затем добавляйте фильтры из исходного запроса по одному и измеряйте производительность.
Пробуйте разные фильтры, оставляя на каждом шаге тот, который выполняется быстрее:

```logsql
_time:5m error | count()
```

```logsql
_time:5m error -"cannot open file" | count()
```

Если какой-то фильтр оказывается медленным, попробуйте заменить его на более быстрый и специфичный.
См. [performance tips](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

Например, медленный фильтр `-"cannot open file"` можно заменить более быстрым
[`contains_any(phrase1, ..., phraseN)`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter),
где `phrase1`, …, `phraseN` — фразы, встречающиеся в нужных логах:

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") | count()
```

После добавления всех необходимых фильтров посмотрите на количество совпадающих логов.
Если оно слишком велико (например, десятки миллионов и больше), стоит добавить более точные фильтры,
чтобы уменьшить объём данных, обрабатываемых [pipes](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).

Например, добавление
[phrase-фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)
по постоянным частям строки из шаблона [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)
может значительно сократить объём данных:

```logsql
_time:5m error contains_any("access denied", "unauthorized", "403") "user_id=(" | count()
```

Затем добавляйте pipes из исходного запроса по одному, каждый раз измеряя время выполнения:

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

Если после добавления очередного фильтра или pipe запрос становится медленным или начинает потреблять много RAM,
вы точно будете знать, какую часть запроса нужно оптимизировать.

Также полезно добавить pipe
[`query_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#query_stats-pipe)
в конец запроса, чтобы понять, какие объёмы данных и каких типов он читает и обрабатывает.

Если вы нашли медленный фильтр или pipe, попробуйте следующие подходы:

* Сопоставление по regex и парсинг JSON — дорогие операции. По возможности используйте более быстрые альтернативы (см. performance tips).
* Сортировка без ограничения (`sort` без `limit`) сохраняет все логи в памяти. Добавьте `limit` или уменьшите входной объём данных.
* Функции с высокой кардинальностью, такие как [`count_uniq()`](https://docs.victoriametrics.com/victorialogs/logsql/#count_uniq-stats), хранят в памяти все уникальные значения. Подумайте, как сократить их количество.
* Большое число групп в [`stats by (...)`](https://docs.victoriametrics.com/victorialogs/logsql/#stats-by-fields) может потреблять много памяти. Отфильтруйте или трансформируйте данные, чтобы уменьшить число групп.
