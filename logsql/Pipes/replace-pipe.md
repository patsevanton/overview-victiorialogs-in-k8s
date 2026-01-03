### Замена подстроки (pipe `replace`)

Конструкция `<q> | replace ("старая", "новая") at поле` [pipe](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) заменяет все вхождения подстроки `старая` на подстроку `новая` в указанном [`поле`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) для всех логов, возвращённых запросом `<q>` [query](https://docs.victoriametrics.com/victorialogs/logsql/#query-syntax).

**Пример:** следующий запрос заменяет все подстроки `secret-password` на `***` в [`поле _msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) для логов за последние 5 минут:

```logsql
_time:5m | replace ("secret-password", "***") at _msg
```

Часть `at _msg` можно опустить, если замена выполняется в [`поле _msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field). Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | replace ("secret-password", "***")
```

Количество замен можно ограничить с помощью `limit N` в конце конструкции `replace`. Например, следующий запрос заменит только первое вхождение подстроки `foo` на `bar` в [поле лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) `baz`:

```logsql
_time:5m | replace ('foo', 'bar') at baz limit 1
```

**Совет по производительности:** рекомендуется использовать более конкретные [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters), чтобы уменьшить число записей логов, передаваемых в `replace`. Подробнее см. в разделе [общие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).


#### Условная замена

Если [pipe `replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe) должен применяться только к некоторым [записям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), добавьте `if (<фильтры>)` после `replace`.  
В `<фильтры>` могут содержаться произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters). Например, следующий запрос заменяет `secret` на `***` в поле `password` **только** если поле `user_type` равно `admin`:

```logsql
_time:5m | replace if (user_type:=admin) ("secret", "***") at password
```
