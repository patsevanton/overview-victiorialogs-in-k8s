## Опции запросов

VictoriaLogs поддерживает следующие опции, которые можно передать в начале [запроса LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>` с помощью синтаксиса `options(opt1=v1, ..., optN=vN) <q>`:

### Опция `concurrency`

VictoriaLogs выполняет каждый запрос параллельно на всех доступных ядрах CPU — это обычно обеспечивает максимальную производительность.  

Иногда требуется уменьшить число используемых ядер CPU — например, чтобы снизить потребление оперативной памяти и/или нагрузку на процессор. Это можно сделать, задав опцию `concurrency` со значением **меньше** числа доступных ядер CPU.  

**Пример:** следующий запрос будет выполняться максимум на 2 ядрах CPU:

```logsql
options(concurrency=2) _time:1d | count_uniq(user_id)
```

Опция `concurrency` применяется индивидуально к каждому узлу `vlstorage` в [кластере VictoriaLogs](https://docs.victoriametrics.com/victorialogs/cluster/).

См. также: [опция запроса `parallel_readers`](https://docs.victoriametrics.com/victorialogs/logsql/#parallel_readers-query-option).

### Опция `parallel_readers`

VictoriaLogs использует параллельные считыватели данных для выполнения запросов. По умолчанию число параллельных считывателей подходит для большинства практических сценариев.  

В отдельных случаях может потребоваться настроить это значение для конкретного запроса — например, чтобы повысить производительность за счёт увеличения числа параллельных считывателей, если логи хранятся в хранилище с высокой задержкой чтения (например, NFS или S3).  

Это делается с помощью опции `parallel_readers`.  

**Пример:** следующий запрос использует 100 параллельных считывателей:

```logsql
options(parallel_readers=100) _time:1d error | count()
```

Если опция `parallel_readers` не задана, но задана [`опция concurrency`](https://docs.victoriametrics.com/victorialogs/logsql/#concurrency-query-option), то число параллельных считывателей будет равно значению `concurrency`.

Число параллельных считывателей по умолчанию можно настроить с помощью флага командной строки `-defaultParallelReaders`.

Опция `parallel_readers` применяется индивидуально к каждому узлу `vlstorage` в [кластере VictoriaLogs](https://docs.victoriametrics.com/victorialogs/cluster/).

**Важно:** слишком большое число параллельных считывателей может привести к избыточному потреблению оперативной памяти и CPU.

### Опция `ignore_global_time_filter`

При запуске через веб‑интерфейс, Grafana или API, которые могут применять глобальный временной диапазон, VictoriaLogs автоматически добавляет в запрос глобальный фильтр `_time:[start,end]`.  

Чтобы **отключить** добавление этого глобального временного фильтра, установите `ignore_global_time_filter=true`.

**Пример:** следующий запрос сохраняет исходную временную логику в теле запроса, не добавляя глобальный фильтр `_time`:

```logsql
options(ignore_global_time_filter=true) _time:>1h | count()
```

### Опция `allow_partial_response`

В режиме кластера VictoriaLogs некоторые узлы `vlstorage` могут временно быть недоступны.  

Установите `allow_partial_response=true`, чтобы возвращать **частичные результаты** от доступных узлов, вместо того чтобы прерывать весь запрос.

**Пример:**

```logsql
options(allow_partial_response=true) _time:1h error | stats count()
```

Это может привести к некорректным результатам, поэтому используйте опцию с осторожностью. Однако лучше применять её явно, чем устанавливать флаг `-search.allowPartialResponse` — так контроль над поведением будет более прозрачным.

### Опция `time_offset`

Опция `time_offset` **вычитает** указанный сдвиг из всех [временных фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#time-filter) в запросе, а затем **добавляет** этот сдвиг к значениям выбранного поля [`_time`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#time-field) перед передачей их в [конвейеры (pipes)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).  

Это позволяет сравнивать результаты запросов за один и тот же промежуток времени, но с разным временным смещением.

Принимает [значения длительности](https://docs.victoriametrics.com/victorialogs/logsql/#duration-values), например: `12h`, `1d`, `1y`.

**Пример:** следующий запрос возвращает число логов с словом `error` за последний час, но **7 дней назад**:

```logsql
options(time_offset=7d) _time:1h error | stats count() as 'errors_7d_ago'
```

### Опция `ignore_global_time_filter` (доп. пример)

Опция `ignore_global_time_filter` позволяет **игнорировать** временной фильтр из аргументов `start` и `end` [HTTP API запросов](https://docs.victoriametrics.com/victorialogs/querying/#http-api) для данного (под)запроса.

**Пример:** следующий запрос возвращает число логов с значениями `user_id`, встреченными в логах за декабрь 2024 года, в диапазоне времени `[start...end)`, переданном в [`/select/logsql/query`](https://docs.victoriametrics.com/victorialogs/querying/#querying-logs):

```logsql
user_id:in(options(ignore_global_time_filter=true) _time:2024-12Z | keep user_id) | count()
```

Подзапрос `in(...)` **без** `options(ignore_global_time_filter=true)` учитывает только значения `user_id` на пересечении декабря 2024 и диапазона `[start...end)`, переданного в [`/select/logsql/query`](https://docs.victoriametrics.com/victorialogs/querying/#querying-logs):

```logsql
user_id:in(_time:2024-12Z | keep user_id) | count()
```

### Опция `allow_partial_response` (доп. пример)

Опцию `allow_partial_response` можно использовать в [настройке кластера VictoriaLogs](https://docs.victoriametrics.com/victorialogs/cluster/) для разрешения частичных ответов, когда некоторые узлы `vlstorage` недоступны для запросов.

**Пример:** следующий запрос возвращает логи за последние 5 минут, даже если некоторые узлы `vlstorage` недоступны (в результате ответ может не содержать логи, хранящиеся на недоступных узлах):

```logsql
options(allow_partial_response=true) _time:5m
```

См. также: [документация по частичным ответам](https://docs.victoriametrics.com/victorialogs/querying/#partial-responses).
