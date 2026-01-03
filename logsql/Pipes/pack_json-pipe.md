### Конвейер `pack_json`

Конструкция `<q> | pack_json as field_name` [конвейер (pipe)](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) упаковывает все [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) каждой записи журнала, возвращённой запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), в объект JSON и сохраняет его в виде строки в указанное поле `field_name`.

Например, следующий запрос упаковывает все поля в объект JSON и сохраняет результат в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) для журналов за последние 5 минут:

```logsql
_time:5m | pack_json as _msg
```

Часть `as _msg` можно опустить, если упакованный объект JSON сохраняется в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | pack_json
```

Если необходимо упаковать в JSON лишь часть полей, их следует перечислить внутри `fields (...)` после `pack_json`. Например, следующий запрос создаёт JSON только с полями `foo` и `bar` и сохраняет результат в поле `baz`:

```logsql
_time:5m | pack_json fields (foo, bar) as baz
```

В `fields (...)` можно передавать префиксы полей, чтобы упаковать только те поля, которые начинаются с указанных префиксов. Например, следующий запрос создаёт JSON со всеми полями, начинающимися на `foo.` или `bar.`:

```logsql
_time:5m | pack_json fields (foo.*, bar.*) as baz
```

Конвейер `pack_json` не изменяет и не удаляет другие поля. Если они не нужны, добавьте [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) после `pack_json`. Например, следующий запрос оставляет только поле `foo`, в котором исходные поля журнала упакованы в JSON:

```logsql
_time:5m | pack_json as foo | fields foo
```
