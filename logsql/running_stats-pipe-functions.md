## Функции `running_stats` для конвейера (pipe)

LogsQL поддерживает следующие функции для конвейера [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe):

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats) — возвращает количество записей в логах.
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-running_stats) — возвращает максимальное значение по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-running_stats) — возвращает минимальное значение по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats) — возвращает сумму числовых значений по указанным [полям логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

### count в `running_stats`

Функция `count()` в конвейере [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions) вычисляет текущее (нарастающее) количество выбранных записей в логах.

**Пример:** следующий запрос добавляет поле `running_logs` к выбранным записям за последние 5 минут:

```logsql
_time:5m | running_stats count() running_logs
```

Можно подсчитать количество записей с непустыми значениями в определённом [поле лога](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model), используя синтаксис `count(fieldName)`.

**Пример:** запрос возвращает текущее количество записей с заполненным полем `username` за последние 5 минут:

```logsql
_time:5m | running_stats count(username) running_logs_with_username
```

Если внутри `count()` перечислить несколько полей, будет подсчитано количество записей, у которых **хотя бы одно** из перечисленных полей не пустое.

**Пример:** запрос возвращает количество записей с непустым полем `username` **или** `password` за последние 5 минут:

```logsql
_time:5m | running_stats count(username, password) running_logs_with_username_or_password
```

Можно подсчитать количество записей с хотя бы одним непустым полем, имеющим общий префикс, с помощью синтаксиса `count(prefix*)`.

**Пример:** запрос возвращает количество записей с хотя бы одним непустым полем с префиксом `foo` за последние 5 минут:

```logsql
_time:5m | running_stats count(foo*)
```

**См. также:**

- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-running_stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-running_stats)

### max в `running_stats`

Функция `max(field1, ..., fieldN)` в конвейере [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions) возвращает текущее (нарастающее) максимальное значение среди всех указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

**Пример:** запрос возвращает текущее максимальное значение поля `duration` за последние 5 минут:

```logsql
_time:5m | running_stats max(duration) running_max_duration
```

Можно вычислить текущее максимальное значение среди всех полей с общим префиксом, используя синтаксис `max(prefix*)`.

**См. также:**

- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-running_stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats)

### min в `running_stats`

Функция `min(field1, ..., fieldN)` в конвейере [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions) возвращает текущее (нарастающее) минимальное значение среди всех указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

**Пример:** запрос возвращает текущее минимальное значение поля `duration` за последние 5 минут:

```logsql
_time:5m | running_stats min(duration) running_min_duration
```

Можно найти текущее минимальное значение среди всех полей с общим префиксом, используя синтаксис `min(prefix*)`.

**См. также:**

- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-running_stats)
- [`sum`](https://docs.victoriametrics.com/victorialogs/logsql/#sum-running_stats)
- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats)

### sum в `running_stats`

Функция `sum(field1, ..., fieldN)` в конвейере [`running_stats`](https://docs.victoriametrics.com/victorialogs/logsql/#running_stats-pipe-functions) вычисляет текущую (нарастающую) сумму числовых значений среди всех указанных [полей логов](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model).

Нечисловые значения игнорируются. Если все значения в полях `field1`, ..., `fieldN` нечисловые, возвращается `NaN`.

**Пример:** запрос возвращает текущую сумму числовых значений поля `duration` за последние 5 минут:

```logsql
_time:5m | running_stats sum(duration) running_sum_duration
```

Можно найти текущую сумму для всех полей с общим префиксом, используя синтаксис `sum(prefix*)`.

**См. также:**

- [`count`](https://docs.victoriametrics.com/victorialogs/logsql/#count-running_stats)
- [`max`](https://docs.victoriametrics.com/victorialogs/logsql/#max-running_stats)
- [`min`](https://docs.victoriametrics.com/victorialogs/logsql/#min-running_stats)
