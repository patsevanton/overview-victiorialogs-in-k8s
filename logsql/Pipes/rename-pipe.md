### Переименование полей (rename pipe)

Если необходимо переименовать некоторые [поля логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), можно использовать конвейер `| rename src1 as dst1, ..., srcN as dstN` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes).

Например, следующий запрос переименовывает поле `host` в `server` для логов за последние 5 минут — в результате в выводе будет поле `server` вместо `host`:

```logsql
_time:5m | rename host as server
```

За один вызов `| rename ...` можно переименовать несколько полей. Например, этот запрос меняет `host` на `instance`, а `app` — на `job`:

```logsql
_time:5m | rename host as instance, app as job
```

Ключевое слово `as` необязательно.

Для удобства вместо `rename` можно использовать ключевое слово `mv`. Например, `_time:5m | mv foo bar` эквивалентно `_time:5m | rename foo as bar`.

Можно переименовать несколько полей с заданным префиксом в поля с другим префиксом. Например, следующий запрос переименовывает все поля, начинающиеся с префикса `foo`, в поля с префиксом `bar`:

```logsql
_time:5m | rename foo* as bar*
```

Также можно удалить общий префикс у некоторых полей. Например, этот запрос убирает префикс `foo` у всех полей, которые с него начинаются:

```logsql
_time:5m | rename foo* as *
```

Кроме того, можно добавить общий префикс ко всем полям. Например, следующий запрос добавляет префикс `foo` ко всем полям:

```logsql
_time:5m | rename * as foo*
```
