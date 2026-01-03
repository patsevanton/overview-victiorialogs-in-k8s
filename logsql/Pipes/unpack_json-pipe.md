### pipe `unpack_json`

`<q> | unpack_json from field_name` — это [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes), который распаковывает JSON вида `{"k1":"v1", ..., "kN":"vN"}` из указанного [`field_name`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)
в результатах [запроса](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax) `<q>` в выходные поля `k1`, …, `kN` с соответствующими значениями `v1`, …, `vN`.

Существующие поля с именами из списка `k1`, …, `kN` будут перезаписаны. Остальные поля остаются без изменений.

Вложенный JSON распаковывается согласно правилам, описанным [здесь](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Например, следующий запрос распаковывает JSON-поля из [`_msg` поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) для логов за последние 5 минут:

```logsql
_time:5m | unpack_json from _msg
```

Часть `from _msg` можно опустить, если JSON-поля извлекаются из [`_msg` поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field).
Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | unpack_json
```

Если нужно извлечь только некоторые поля из JSON, их можно перечислить в `fields (...)`. Например, следующий запрос распаковывает только поля `foo` и `bar`
из JSON, сохранённого в [лог-поле](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `my_json`:

```logsql
_time:5m | unpack_json from my_json fields (foo, bar)
```

Если требуется извлечь все поля с общим префиксом, можно использовать синтаксис `fields(prefix*)`.

Если необходимо сохранить исходные непустые значения полей, добавьте `keep_original_fields` в конец `unpack_json ...`. Например,
следующий запрос сохраняет исходные непустые значения полей `ip` и `host` вместо их перезаписи распакованными значениями:

```logsql
_time:5m | unpack_json from foo fields (ip, host) keep_original_fields
```

Добавьте `skip_empty_results` в конец `unpack_json ...`, если исходные значения полей должны сохраняться, когда соответствующие распакованные значения пустые.
Например, следующий запрос сохраняет исходные значения полей `ip` и `host`, если распакованные значения пусты:

```logsql
_time:5m | unpack_json fields (ip, host) skip_empty_results
```

**Совет по производительности:** если нужно извлечь одно поле из длинного JSON, быстрее использовать [`extract` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe). Например, следующий запрос извлекает поле `"ip"` из JSON,
хранящегося в [`_msg` поле](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), с максимальной скоростью:

```
_time:5m | extract '"ip":<ip>'
```

Если нужно убедиться, что распакованные JSON-поля не конфликтуют с существующими полями, укажите общий префикс для всех извлекаемых полей,
добавив `result_prefix "prefix_name"` к `unpack_json`. Например, следующий запрос добавляет префикс `foo_` ко всем полям,
распакованным из `foo`:

```logsql
_time:5m | unpack_json from foo result_prefix "foo_"
```

### Советы по производительности

* С точки зрения производительности и потребления ресурсов лучше загружать уже разобранные JSON-логи в VictoriaLogs
  в соответствии с [поддерживаемой моделью данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
  чем загружать неразобранные JSON-строки и затем парсить их во время выполнения запроса с помощью [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe).

* Рекомендуется использовать более точные [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters),
  чтобы уменьшить количество записей, передаваемых в `unpack_json`.
  Подробности см. в [общих советах по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

#### Условный `unpack_json`

Если [`unpack_json` pipe](https://docs.victoriametrics.com/victorialogs/logsql/#unpack_json-pipe) должен применяться только к некоторым [лог-записям](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model),
добавьте `if (<filters>)` после `unpack_json`.

`<filters>` может содержать произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters). Например, следующий запрос распаковывает JSON-поля из поля `foo` только если поле `ip` в текущей записи лога не задано или пустое:

```logsql
_time:5m | unpack_json if (ip:"") from foo
```
