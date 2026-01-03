
## Интеграция: Grafana, vmalert, OpenTelemetry

- Grafana: используйте официальный плагин VictoriaLogs Datasource для дашбордов и визуализации LogsQL-запросов.
- vmalert: позволяет строить алерты по логам (через `/select/logsql/stats_query` API). Пример правила:

```yaml
groups:
  - name: ServiceLog
    type: vlogs
    interval: 5m
    rules:
      - alert: HasErrorLog
        expr: 'env: "prod" AND status:~"error|warn" | stats by (service, kubernetes.pod) count() as errorLog | filter errorLog:>0'
        annotations:
          description: 'Service {{$labels.service}} generated {{$labels.errorLog}} error logs in the last 5 minutes'
```

- OpenTelemetry: VictoriaLogs совместим с OpenTelemetry ingestion (через vlinsert/collector).


## Безопасность, хранение и retention

- Настройте TLS/mTLS для внутренних коммуникаций в кластерной конфигурации.
- Используйте авторизацию (vmauth / реверс-прокси) для защиты HTTP API.
- Политики хранения: per-day partitions, snapshot/restore через internal endpoints; возможен retention по месту на диске.


## Полезные ссылки

- Официальная документация VictoriaLogs: https://docs.victoriametrics.com/victorialogs/
- LogsQL: https://docs.victoriametrics.com/victorialogs/logsql/
- vmalert (alerting): https://docs.victoriametrics.com/victoriametrics/vmalert/


## Заключение

VictoriaLogs — зрелое решение для production-логирования в Kubernetes. Оно даёт высокую производительность при небольших ресурсных затратах, обеспечивает удобный язык запросов и интеграцию с экосистемой (Grafana, vmalert, OpenTelemetry). Рекомендуется протестировать чарт на реальных объёмах данных перед переносом в production и настроить TLS/авторизацию для защиты данных.
