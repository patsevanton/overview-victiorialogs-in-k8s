### Конвейер `fields` (выбор полей)

По умолчанию в ответе возвращаются **все поля лога** (см. [модель данных](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)).

Выбрать конкретный набор полей лога можно с помощью конвейера `| fields поле1, ..., полеN` (см. [конвейеры](https://docs.victoriametrics.com/victorialogs/logsql/#pipes)).

Например, следующий запрос выбирает из логов за последние 5 минут **только поля** `host` и [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field):

```logsql
_time:5m | fields host, _msg
```

Для удобства вместо `fields` можно использовать `keep`. Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | keep host, _msg
```

В списке полей допускается использовать **шаблоны с подстановкой** (wildcard). Например, следующий запрос оставит **все поля, имена которых начинаются с префикса `foo`**, а остальные поля удалит:

```logsql
_time:5m | fields foo*
```
