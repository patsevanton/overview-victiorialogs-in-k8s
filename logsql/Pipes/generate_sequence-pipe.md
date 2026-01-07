## Конвейер generate_sequence

Пропускает все результаты запроса и генерирует N выходных логов с полем `_msg`, содержащим целочисленную последовательность от 0 до N-1. Полезен для тестирования и отладки.

**Примеры:**

```logsql
* | generate_sequence 1000 | math round(rand()*10) as rand_num | stats by (rand_num) count() hits | sort by (rand_num)
```
