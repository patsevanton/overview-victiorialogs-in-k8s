### Конвейер `replace_regexp`

Конструкция  
```
<q> | replace_regexp ("regexp", "replacement") at field
```
[конвейер](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) заменяет все подстроки, соответствующие заданному регулярному выражению `regexp`, на строку `replacement` в указанном поле [`field`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) для всех логов, возвращённых запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

- Регулярное выражение `regexp` должно соответствовать синтаксису [RE2](https://github.com/google/re2/wiki/Syntax).
- В строке замены `replacement` могут использоваться плейсхолдеры `$N` или `${N}`, которые подставляются значениями `N`-й захватывающей группы из `regexp`.

**Пример:** следующий запрос заменяет все подстроки, начинающиеся с `host-` и заканчивающиеся на `-foo`, на содержимое между `host-` и `-foo` в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) для логов за последние 5 минут:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1") at _msg
```

Часть `at _msg` можно опустить, если замена производится в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | replace_regexp ("host-(.+?)-foo", "$1")
```

Количество замен можно ограничить с помощью `limit N` в конце `replace_regexp`. Например, следующий запрос заменяет только первую подстроку `password: ...`, заканчивающуюся пробелом, на пустую строку в поле лога `baz`:

```logsql
_time:5m | replace_regexp ('password: [^ ]+', '') at baz limit 1
```

### Советы по производительности

- По возможности используйте [конвейер `replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) вместо `replace_regexp`, так как он работает быстрее.
- Рекомендуется применять более конкретные [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters), чтобы уменьшить число записей, передаваемых в `replace_regexp`.  
  Подробнее — в разделе [общих советов по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

#### Условный `replace_regexp`

Если конвейер [`replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe) должен применяться лишь к некоторым [записям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), добавьте `if (<filters>)` после `replace_regexp`.  
В `<filters>` могут быть указаны произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).

**Пример:** следующий запрос заменяет подстроки `password: ...`, заканчивающиеся пробелом, на `***` в поле `foo` — но только если поле `user_type` равно `admin`:

```logsql
_time:5m | replace_regexp if (user_type:=admin) ("password: [^ ]+", "***") at foo
```
