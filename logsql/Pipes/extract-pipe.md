## Оператор extract (извлечение данных)

Извлекает текст из указанного поля и сохраняет в новые поля согласно шаблону. Существующие поля не изменяются. Если применяется к `_msg`, часть `from _msg` можно опустить.

**Примеры:**

```logsql
_time:1d error | extract "ip=<ip> " from _msg | top 10 (ip)
_time:1d error | extract "ip=<ip> "
_time:5m | extract '"ip":"<ip>"'
_time:5m | extract 'ip=<ip> ' keep_original_fields
_time:5m | extract 'ip=<ip> ' from foo skip_empty_results
_time:5m | extract if (ip:"") "ip=<ip> "
```

**Плейсхолдеры:** `<поле>` — именованный, `<_>` — анонимный, `plain:` — отключение удаления кавычек.
