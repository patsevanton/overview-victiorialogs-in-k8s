### Фильтр потоков

VictoriaLogs предоставляет оптимизированный способ выбора логов, относящихся к конкретным **[потокам логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)**.

Это делается с помощью фильтра `{...}`, который может содержать произвольный **[селектор меток, совместимый с Prometheus](https://docs.victoriametrics.com/victoriametrics/keyconcepts/#filtering)**, применяемый к полям, связанным с **[потоками логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)**.

Например, следующий запрос выбирает **[записи логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model)**, у которых поле `app` равно `nginx`:

```logsql
{app="nginx"}
```

Этот запрос эквивалентен следующему запросу с **[фильтром точного совпадения (`exact`)](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter)**, однако верхний вариант обычно работает значительно быстрее:

```logsql
app:="nginx"
```

Фильтр потока поддерживает синтаксис `{label in (v1,...,vN)}` и `{label not_in (v1,...,vN)}`.  
Он эквивалентен `{label=~"v1|...|vN"}` и `{label!~"v1|...|vN"}` соответственно. Значения `v1`, ..., `vN` корректно экранируются внутри регулярного выражения.

Например, `{app in ("nginx", "foo.bar")}` эквивалентно `{app=~"nginx|foo\\.bar"}` — обратите внимание, что символ `.` корректно экранирован.

Разрешается добавлять префикс `_stream:` перед фильтром `{...}`, чтобы явно указать, что фильтрация выполняется по **[полю лога `_stream`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#stream-fields)**.  
Следующий фильтр эквивалентен `{app="nginx"}`:

```logsql
_stream:{app="nginx"}
```

**Советы по производительности:**

- Рекомендуется использовать максимально конкретный фильтр `{...}`, который соответствует наименьшему числу потоков логов — это сократит объём данных, сканируемых остальными фильтрами в запросе.

- Хотя LogsQL поддерживает произвольное число фильтров `{...}` на любом уровне **[логических фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter)**, рекомендуется указывать **единственный** фильтр `{...}` на верхнем уровне запроса.
