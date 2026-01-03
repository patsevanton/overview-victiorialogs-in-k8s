### Фильтр диапазона (range filter)

Если нужно отфильтровать сообщения журнала по полю, содержащему **только числовые значения**, можно использовать фильтр `range()`.

Например, если поле `request.duration` хранит длительность запроса в секундах, для поиска записей журнала с длительностью более $4{,}2$ секунды подойдёт такой запрос на языке LogsQL:

```logsql
request.duration:range(4.2, Inf)
```

Этот запрос можно сократить, используя [фильтр сравнения диапазонов](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter):

```logsql
request.duration:>4.2
```

Нижняя и верхняя границы в `range(нижняя, верхняя)` по умолчанию **исключаются**. Если их нужно включить, замените соответствующие круглые скобки на квадратные:

- `range[1, 10)` — включает `1` в диапазон совпадения;
- `range(1, 10]` — включает `10` в диапазон совпадения;
- `range[1, 10]` — включает и `1`, и `10` в диапазон совпадения.

Границы диапазона могут содержать любые [поддерживаемые числовые значения](https://docs.victoriametrics.com/victorialogs/logsql/#numeric-values).

**Важно:** фильтр `range()` **не сопоставляет** [поля журнала](https://docs.victoriametrics.com/victorialogs/keyconcepts/#data-model) с нечисловыми значениями наряду с числовыми. Например, `range(1, 10)` не подойдёт для сообщения журнала `the request took 4.2 seconds`, поскольку число `4.2` окружено другим текстом.

Чтобы решить эту проблему, извлеките числовое значение из сообщения с помощью конвейера [`extract`](https://docs.victoriametrics.com/victorialogs/logsql/#extract-pipe), а затем примените фильтр `range()` к извлечённому полю.

**Советы по производительности:**

- Лучше запрашивать **чисто числовое поле** вместо извлечения числового поля из текстового поля с помощью [преобразований](https://docs.victoriametrics.com/victorialogs/logsql/#transformations) во время выполнения запроса.
- См. [другие советы по производительности](https://docs.victoriametrics.com/victorialogs/logsql/#performance-tips).

**См. также:**

- [Фильтр сравнения диапазонов](https://docs.victoriametrics.com/victorialogs/logsql/#range-comparison-filter);
- [Фильтр диапазона IPv4](https://docs.victoriametrics.com/victorialogs/logsql/#ipv4-range-filter);
- [Строковый фильтр диапазона](https://docs.victoriametrics.com/victorialogs/logsql/#string-range-filter);
- [Фильтр диапазона длины](https://docs.victoriametrics.com/victorialogs/logsql/#length-range-filter);
- [Логический фильтр](https://docs.victoriametrics.com/victorialogs/logsql/#logical-filter).
