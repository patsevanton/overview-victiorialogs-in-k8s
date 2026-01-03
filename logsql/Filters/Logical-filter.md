### Логический фильтр

Базовые фильтры LogsQL [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters) можно объединять в более сложные с помощью следующих логических операций:

- `q1 AND q2` — отбирает записи журнала, которые возвращаются **и** `q1`, **и** `q2`. С помощью операции `AND` можно объединить произвольное число [фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#filters).  
  Например, `error AND file AND app` находит [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), которые одновременно содержат слова `error`, `file` и `app`.  
  Операция `AND` часто используется в запросах LogsQL, поэтому допускается опускать слово `AND`.  
  Например, `error file app` эквивалентно `error AND file AND app`. См. также фильтр [`contains_all`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_all-filter).

- `q1 OR q2` — объединяет записи журнала, возвращаемые `q1` **или** `q2`. С помощью операции `OR` можно объединить произвольное число [фильтров](https://docs.victoriametrics.com/victorialogs/logsql/#filters).  
  Например, `error OR warning OR info` находит [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), которые содержат **хотя бы одно** из слов: `error`, `warning` или `info`. См. также фильтр [`contains_any`](https://docs.victoriametrics.com/victorialogs/logsql/#contains_any-filter).

- `NOT q` — возвращает все записи журнала, **кроме** тех, что соответствуют `q`. Например, `NOT info` возвращает все [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), которые **не содержат** слово `info`.  
  Операция `NOT` часто используется в запросах LogsQL, поэтому в запросах допускается заменять `NOT` на `-` и `!`.  
  Например, `-info` и `!info` эквивалентны `NOT info`.  
  Символ `!` **должен** использоваться вместо `-` перед фильтрами [`=`](https://docs.victoriametrics.com/victorialogs/logsql/#exact-filter) и [`~`](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter), например `!=` и `!~`.

**Приоритет операций:**  
- `NOT` имеет наивысший приоритет,  
- `AND` — средний,  
- `OR` — наименьший.  

Порядок приоритетов можно изменить с помощью скобок. Например, `NOT info OR debug` интерпретируется как `(NOT info) OR debug`, то есть отбирает [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), которые не содержат слово `info`, а также сообщения со словом `debug` (которые могут содержать и `info`).  
Это не всегда соответствует ожиданиям пользователя. В таком случае запрос можно переписать как `NOT (info OR debug)` — он корректно вернёт сообщения журнала **без** слов `info` и `debug`.

LogsQL поддерживает произвольно сложные логические запросы с любым сочетанием операций `AND`, `OR`, `NOT` и скобок.

**По умолчанию** логические фильтры применяются к полю [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), если внутренние фильтры явно не указывают нужное [поле журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с помощью синтаксиса `имя_поля:фильтр`.  
Например, `(error OR warn) AND host.hostname:host123` интерпретируется как `(_msg:error OR _msg:warn) AND host.hostname:host123`.

Можно указать одно [поле журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) для нескольких фильтров с помощью следующего синтаксиса:

```logsql
имя_поля:(q1 OR q2 OR ... qN)
```

Например, `log.level:error OR log.level:warning OR log.level:info` можно заменить более коротким запросом: `log.level:(error OR warning OR info)`.

**Советы по производительности:**

- VictoriaLogs выполняет логические операции **слева направо**, поэтому рекомендуется размещать **наиболее специфичные и быстрые** фильтры (такие как [фильтр по слову](https://docs.victoriametrics.com/victorialogs/logsql/#word-filter) и [фильтр по фразе](https://docs.victoriametrics.com/victorialogs/logsql/#phrase-filter)) **слева**, а **менее специфичные и медленные** (такие как [фильтр по регулярному выражению](https://docs.victoriametrics.com/victorialogs/logsql/#regexp-filter) и [фильтр без учёта регистра](https://docs.victoriametrics.com/victorialogs/logsql/#case-insensitive-filter)) — **справа**.  
  Например, если нужно найти [сообщения журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field) со словом `error`, которые соответствуют регулярному выражению `/foo/(bar|baz)`, с точки зрения производительности лучше использовать запрос `error ~"/foo/(bar|baz)"`, а не `~"/foo/(bar|baz)" error`.  
  **Наиболее специфичный фильтр** — это тот, который отбирает наименьшее число записей журнала по сравнению с другими фильтрами.

- См. [другие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).
