## Учебное пособие по LogsQL

### Основы запросов LogsQL

Самый простой запрос — слово, которое нужно найти в сообщении лога (поле `_msg`). Для выполнения запросов рекомендуется использовать утилиту `vlogscli`.

**Примеры:**

```logsql
error
"and"
"error: cannot find file"
```

### Фильтр по времени

Рекомендуется добавлять фильтр по времени для ограничения поиска.

**Примеры:**

```logsql
error AND _time:5m
_time:5m error
```

### Сортировка и ограничение результатов

**Примеры:**

```logsql
_time:5m error | sort by (_time)
_time:5m error | sort by (_time) desc | limit 10
```

### Выбор полей

**Примеры:**

```logsql
error _time:5m | fields _time, _stream, _msg
```

### Исключение записей

**Примеры:**

```logsql
_time:5m error NOT buggy_app
_time:5m error -buggy_app
_time:5m error -(buggy_app OR foobar)
```

### Запросы по полям

**Примеры:**

```logsql
_time:5m log.level:error -(buggy_app OR foobar)
_time:5m log.level:error -app:(buggy_app OR foobar)
```

### Оптимизация запросов

Используйте фильтр по потокам для повышения производительности:

```logsql
_time:5m log.level:error {app!~"buggy_app|foobar"}
```

### Статистические функции

**Примеры:**

```logsql
_time:5m error | stats count() logs_with_error
```

### Ключевые понятия

**Слово (Word):** LogsQL разбивает все поля лога на слова, разделённые небуквенными символами. Слова могут содержать любые символы UTF‑8.
