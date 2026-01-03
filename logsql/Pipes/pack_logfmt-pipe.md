### Конвейер `pack_logfmt`

Конструкция  
```
<q> | pack_logfmt as field_name
```  
[конвейер](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) упаковывает все [поля](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) каждой записи журнала, возвращённой запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax), в сообщение формата [logfmt](https://brandur.org/logfmt) и сохраняет его в виде строки в указанном поле `field_name`.

**Пример.** Следующий запрос упаковывает все поля в сообщение формата [logfmt](https://brandur.org/logfmt) и сохраняет результат в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) для журналов за последние 5 минут:

```logsql
_time:5m | pack_logfmt as _msg
```

Часть `as _msg` можно опустить, если упакованное сообщение сохраняется в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | pack_logfmt
```

Если нужно упаковать в [logfmt](https://brandur.org/logfmt) лишь подмножество полей, их следует перечислить внутри `fields (...)` после `pack_logfmt`.

**Пример.** Нижеприведённый запрос формирует сообщение [logfmt](https://brandur.org/logfmt), включающее только поля `foo` и `bar`, и сохраняет результат в поле `baz`:

```logsql
_time:5m | pack_logfmt fields (foo, bar) as baz
```

В `fields (...)` можно передавать префиксы полей — тогда будут упакованы лишь те поля, которые начинаются с указанных префиксов.

**Пример.** Следующий запрос строит сообщение `logfmt`, включающее все поля, начинающиеся с `foo.` или `bar.`:

```logsql
_time:5m | pack_logfmt fields (foo.*, bar.*) as baz
```

Конвейер `pack_logfmt` не изменяет и не удаляет другие поля. Если они не нужны, добавьте [`| fields ...`](https://docs.victoriametrics.com/victorialogs/logsql/#fields-pipe) после `pack_logfmt`.

**Пример.** Нижеприведённый запрос оставляет только поле `foo`, при этом исходные поля журнала упакованы в формат [logfmt](https://brandur.org/logfmt):

```logsql
_time:5m | pack_logfmt as foo | fields foo
```
