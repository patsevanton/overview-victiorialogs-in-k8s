### pipe `unpack_syslog`

`<q> | unpack_syslog from field_name` — это [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes), который распаковывает сообщения [syslog](https://en.wikipedia.org/wiki/Syslog)
из указанного [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) в результатах [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>`.

Поддерживаются следующие форматы Syslog:

* [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164), также известный как
  `<PRI>MMM DD hh:mm:ss HOSTNAME APP-NAME[PROCID]: MESSAGE`
* [RFC5424](https://datatracker.ietf.org/doc/html/rfc5424), также известный как
  `<PRI>1 TIMESTAMP HOSTNAME APP-NAME PROCID MSGID [STRUCTURED-DATA] MESSAGE`

Распаковываются следующие поля:

* `level` — извлекается из `PRI`.
* `priority` — извлекается из `PRI`.
* `facility` — вычисляется как `PRI / 8`.
* `facility_keyword` — строковое представление поля `facility` согласно [этой документации](https://en.wikipedia.org/wiki/Syslog#Facility).
* `severity` — вычисляется как `PRI % 8`.
* `format` — `rfc3164` или `rfc5424` в зависимости от распознанного формата Syslog.
* `timestamp` — временная метка в формате [ISO8601](https://en.wikipedia.org/wiki/ISO_8601).
  Временная метка `MMM DD hh:mm:ss` из [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164)
  автоматически преобразуется в формат ISO8601 с предположением, что она относится к последним 12 месяцам.
* `hostname`
* `app_name`
* `proc_id`
* `msg_id`
* `message`

Часть `<PRI>` является необязательной. Если она отсутствует, то поля `priority`, `facility` и `severity` не заполняются.

Блок `[STRUCTURED-DATA]` разбирается в поля с именами
`SD-ID.param1`, `SD-ID.param2`, …, `SD-ID.paramN` и соответствующими значениями
в соответствии со [спецификацией](https://datatracker.ietf.org/doc/html/rfc5424#section-6.3).

Если `app_name` равен `CEF`, а поле `message` содержит данные в формате Common Event Format для SIEM
(см. [CEF for Syslog](https://www.microfocus.com/documentation/arcsight/arcsight-smartconnectors-8.3/cef-implementation-standard/Content/CEF/Chapter%201%20What%20is%20CEF.htm)),
то они автоматически разбираются в следующие поля:

* `cef.version` — версия CEF
* `cef.device_vendor` — производитель устройства
* `cef.device_product` — продукт устройства
* `cef.device_version` — версия устройства
* `cef.device_event_class_id` — идентификатор класса события
* `cef.name` — имя CEF
* `cef.severity` — уровень серьёзности

Необязательные поля расширений разбираются в виде
`cef.extension.<key>=<value>`.

Например, следующий запрос распаковывает сообщения [syslog](https://en.wikipedia.org/wiki/Syslog)
из поля [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
по всем логам за последние 5 минут:

```logsql
_time:5m | unpack_syslog from _msg
```

Часть `from _msg` можно опустить, если сообщение syslog извлекается из поля `_msg`.
Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | unpack_syslog
```

По умолчанию временные метки в формате [RFC3164](https://datatracker.ietf.org/doc/html/rfc3164)
преобразуются в локальный часовой пояс. Смещение часового пояса можно изменить с помощью опции `offset`.
Например, следующий запрос добавляет 5 часов и 30 минут к распакованным временным меткам `rfc3164`:

```logsql
_time:5m | unpack_syslog offset 5h30m
```

Если необходимо сохранить исходные непустые значения полей, добавьте `keep_original_fields`
в конец `unpack_syslog ...`:

```logsql
_time:5m | unpack_syslog keep_original_fields
```

Если нужно гарантировать, что распакованные поля syslog не конфликтуют с уже существующими полями,
укажите общий префикс для всех извлечённых полей, добавив
`result_prefix "prefix_name"` к `unpack_syslog`.
Например, следующий запрос добавляет префикс `foo_` ко всем полям,
распакованным из поля `foo`:

```logsql
_time:5m | unpack_syslog from foo result_prefix "foo_"
```

#### Советы по производительности

* С точки зрения производительности и потребления ресурсов лучше загружать уже разобранные сообщения
  [syslog](https://en.wikipedia.org/wiki/Syslog) в VictoriaLogs
  в соответствии с [поддерживаемой моделью данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
  чем загружать неразобранные строки syslog и затем разбирать их во время выполнения запроса с помощью pipe `unpack_syslog`.

* Рекомендуется использовать более специфичные [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters),
  чтобы уменьшить количество записей, передаваемых в `unpack_syslog`.
  Подробности см. в [общих советах по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).


### Условный `unpack_syslog`

Если pipe [`unpack_syslog`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
должен применяться только к некоторым [записям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
добавьте `if (<filters>)` после `unpack_syslog`.

`<filters>` может содержать любые [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).
Например, следующий запрос распаковывает поля syslog из поля `foo`
только в том случае, если поле `hostname` в текущей записи лога не задано или пустое:

```logsql
_time:5m | unpack_syslog if (hostname:"") from foo
```
