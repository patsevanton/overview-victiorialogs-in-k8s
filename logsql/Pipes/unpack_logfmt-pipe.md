### pipe unpack_logfmt

`<q> | unpack_logfmt from field_name` — это [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes), который распаковывает поля формата `k1=v1 ... kN=vN` [logfmt](https://brandur.org/logfmt)
из указанного [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) в результатах [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>` в поля `k1`, …, `kN`
с соответствующими значениями `v1`, …, `vN`.
Существующие поля с именами из списка `k1`, …, `kN` будут перезаписаны. Остальные поля остаются без изменений.

Например, следующий запрос распаковывает поля [logfmt](https://brandur.org/logfmt) из
[поля `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field)
для логов за последние 5 минут:

```logsql
_time:5m | unpack_logfmt from _msg
```

Часть `from _msg` можно опустить, если поля logfmt распаковываются из
[поля `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | unpack_logfmt
```

Если нужно распаковать только некоторые поля из logfmt, их можно перечислить в `fields (...)`.
Например, следующий запрос извлекает только поля `foo` и `bar`
из logfmt, хранящегося в поле `my_logfmt`:

```logsql
_time:5m | unpack_logfmt from my_logfmt fields (foo, bar)
```

Если требуется извлечь все поля с общим префиксом, можно использовать синтаксис `fields(prefix*)`.

Если необходимо сохранить исходные непустые значения полей, добавьте `keep_original_fields`
в конец `unpack_logfmt ...`. Например, следующий запрос сохраняет исходные непустые значения
полей `ip` и `host`, вместо того чтобы перезаписывать их распакованными значениями:

```logsql
_time:5m | unpack_logfmt from foo fields (ip, host) keep_original_fields
```

Добавьте `skip_empty_results` в конец `unpack_logfmt ...`, если исходные значения полей
должны сохраняться в случае, когда соответствующие распакованные значения пустые.
Например, следующий запрос сохраняет исходные значения полей `ip` и `host`
при пустых распакованных значениях:

```logsql
_time:5m | unpack_logfmt fields (ip, host) skip_empty_results
```

**Совет по производительности:** если нужно извлечь одно поле из длинной строки
[logfmt](https://brandur.org/logfmt), быстрее использовать
[pipe `extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe).
Например, следующий запрос извлекает поле `"ip"` из строки logfmt,
хранящейся в
[поле `_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```
_time:5m | extract ' ip=<ip>'
```

Если нужно убедиться, что распакованные поля logfmt не конфликтуют с уже существующими полями,
можно задать общий префикс для всех извлекаемых полей, добавив
`result_prefix "prefix_name"` к `unpack_logfmt`.
Например, следующий запрос добавляет префикс `foo_` ко всем полям,
распакованным из поля `foo`:

```logsql
_time:5m | unpack_logfmt from foo result_prefix "foo_"
```

### Советы по производительности

* С точки зрения производительности и использования ресурсов лучше загружать уже распарсенные
  логи [logfmt](https://brandur.org/logfmt) в VictoriaLogs в соответствии с
  [поддерживаемой моделью данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
  чем загружать нераспарсенные строки logfmt и затем разбирать их во время выполнения запроса
  с помощью [pipe `unpack_logfmt`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe).

* Рекомендуется использовать более специфичные
  [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters),
  чтобы уменьшить количество записей, передаваемых в `unpack_logfmt`.
  Подробнее см. в [общих советах по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

См. также:

* [Условный unpack_logfmt](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-unpack_logfmt)
* [pipe `unpack_json`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe)
* [pipe `unpack_syslog`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_syslog-pipe)
* [pipe `extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

---

#### Условный unpack_logfmt

Если [pipe `unpack_logfmt`](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_logfmt-pipe)
нужно применять только к некоторым
[записям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
добавьте `if (<filters>)` после `unpack_logfmt`.

`<filters>` может содержать любые
[фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).
Например, следующий запрос распаковывает поля logfmt из поля `foo`
только если поле `ip` в текущей записи лога не задано или пустое:

```logsql
_time:5m | unpack_logfmt if (ip:"") from foo
```
