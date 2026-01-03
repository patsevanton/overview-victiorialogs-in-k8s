### Труба `format` (format pipe)

Конструкция

```
<q> | format "шаблон" as result_field
```

[Труба](https://docs.victoriametrics.com/victorialogs/logsql/#pipes) `format` объединяет [поля логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) из результатов запроса `<q>` согласно шаблону `pattern` и сохраняет результат в поле `result_field`.

**Пример:** следующий запрос сохраняет текст `request from <ip>:<port>` в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), подставляя вместо `<ip>` и `<port>` соответствующие значения из [полей лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model):

```logsql
_time:5m | format "request from <ip>:<port>" as _msg
```

Если результат шаблона `format` сохраняется в поле [`_msg`](https://docs.victoriametrics.com/victorialogs/keyconcepts/#message-field), часть `as _msg` можно опустить. Следующий запрос эквивалентен предыдущему:

```logsql
_time:5m | format "request from <ip>:<port>"
```

Для строковых полей доступны дополнительные правила форматирования:

- **Количество секунд в значении длительности** — добавьте `duration_seconds:` перед именем соответствующего поля. Отформатированное число будет дробным, если значение длительности содержит ненулевые миллисекунды, микросекунды или наносекунды.

- **Строка в формате JSON с кавычками** — добавьте `q:` перед именем поля.  
  Например, следующий запрос формирует корректно закодированный JSON‑объект из полей лога `_msg` и `stacktrace` и сохраняет его в выходное поле `my_json`:

  ```logsql
  _time:5m | format '{"_msg":<q:_msg>,"stacktrace":<q:stacktrace>}' as my_json
  ```

- **Верхний и нижний регистр** — добавьте `uc:` или `lc:` перед именем поля.  
  Например, следующий запрос сохраняет значение поля `foo` в верхнем регистре и значение поля `bar` в нижнем регистре в поле `result`:

  ```logsql
  _time:5m | format 'uppercase foo: <uc:foo>, lowercase bar: <lc:bar>' as result
  ```

- **Кодирование и декодирование URL** (percent encoding) — добавьте `urlencode:` или `urldecode:` перед именем поля.  
  Например, следующий запрос корректно кодирует поле `user` в параметре URL:

  ```logsql
  _time:5m | format 'url: http://foo.com/?user=<urlencode:user>'
  ```

- **Шестнадцатеричное кодирование и декодирование** — добавьте `hexencode:` или `hexdecode:` перед именем поля.  
  Например, следующий запрос кодирует поле `password` в шестнадцатеричном формате:

  ```logsql
  _time:5m | format 'hex-encoded password: <hexencode:password>'
  ```

- **Кодирование и декодирование Base64** — добавьте `base64encode:` или `base64decode:` перед именем поля.  
  Например, следующий запрос кодирует поле `password` в формате Base64:

  ```logsql
  _time:5m | format 'base64-encoded password: <base64encode:password>'
  ```

- **Преобразование шестнадцатеричного числа в десятичное** — добавьте `hexnumdecode:` перед именем поля.  
  Например: `format "num=<hexnumdecode:some_hex_field>"`.

Числовые поля можно преобразовать в следующие строковые представления с помощью трубы `format`:

- **Время в формате RFC3339** — добавьте `time:` перед именем поля, содержащего [Unix‑время](https://en.wikipedia.org/wiki/Unix_time).  
  Числовой timestamp может быть в секундах, миллисекундах, микросекундах или наносекундах — точность определяется автоматически на основе значения. Поддерживаются как целые, так и дробные числа.  
  Например: `format "time=<time:timestamp>"`.

- **Человекочитаемая длительность** — добавьте `duration:` перед именем числового поля, содержащего длительность в наносекундах.  
  Например: `format "duration=<duration:duration_nsecs>"`. Длительность можно преобразовать в наносекунды с помощью [трубы `math`](https://docs.victoriametrics.com/victorialogs/logsql/#math-pipe).

- **IPv4** — добавьте `ipv4:` перед именем поля, содержащего `uint32`‑представление IPv4‑адреса.  
  Например: `format "ip=<ipv4:ip_num>"`.

- **Шестнадцатеричное число с нулями до 64 бит** — добавьте `hexnumencode:` перед именем поля.  
  Например: `format "hex_num=<hexnumencode:some_field>"`.

Добавьте `keep_original_fields` в конец конструкции `format ... as result_field`, если исходное непустое значение поля `result_field` должно быть сохранено, а не перезаписано результатом `format`.  
Например, следующий запрос добавляет отформатированный результат в поле `foo`, только если оно было пустым или отсутствовало:

```logsql
_time:5m | format 'some_text' as foo keep_original_fields
```

Добавьте `skip_empty_results` в конец `format ...`, если пустые результаты не должны записываться в вывод.  
Например, следующий запрос добавляет отформатированный результат в поле `foo`, когда хотя бы одно из полей `field1` или `field2` не пустое, сохраняя при этом исходное значение `foo`:

```logsql
_time:5m | format "<field1><field2>" as foo skip_empty_results
```

**Совет по производительности:** рекомендуется использовать более конкретные [фильтры логов](https://docs.victoriametrics.com/victorialogs/logsql/#filters), чтобы уменьшить количество записей лога, передаваемых в `format`. Подробнее см. в разделе [общие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

**См. также:**

- [Условное форматирование](https://docs.victoriametrics.com/victorialogs/logsql/#conditional-format)
- [Труба `replace`](https://docs.victoriametrics.com/victorialogs/logsql/#replace-pipe)
- [Труба `replace_regexp`](https://docs.victoriametrics.com/victorialogs/logsql/#replace_regexp-pipe)
- [Труба `extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe)

#### Условное форматирование

Если [труба `format`](https://docs.victoriametrics.com/victorialogs/logsql/#format-pipe) должна применяться только к некоторым [записям лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), добавьте `if (<фильтры>)` сразу после слова `format`.  
В `<фильтры>` могут содержаться произвольные [фильтры](https://docs.victoriametrics.com/victorialogs/logsql/#filters).  

**Пример:** следующий запрос сохраняет отформатированный результат в поле `message` только если поля `ip` и `host` не пустые, в противном случае исходное поле `message` не изменяется:

```logsql
_time:5m | format if (ip:* and host:*) "request from <ip>:<host>" as message
```
