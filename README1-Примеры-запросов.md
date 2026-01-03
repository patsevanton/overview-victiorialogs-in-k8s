## Примеры запросов

1) Счётчики по статусам для namespace nginx-log-generator:

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.status_code) count() as requests | sort by (requests desc)
```

2) Топ медленных URL по времени ответа:

```
kubernetes.pod_namespace:"nginx-log-generator" | stats by (http.url) max(http.request_time) as max_time | sort by (max_time desc) | limit 10
```

3) IP с наибольшим количеством ошибок:

```
kubernetes.pod_namespace:"nginx-log-generator" | http.status_code:>=400 | stats by (nginx.remote_addr) count() as errors | sort by (errors desc) | limit 10
```

4) Доля ошибок (percent):

```
kubernetes.pod_namespace:"nginx-log-generator" |
  stats count() as total, count() if (http.status_code:>=400) as errors |
  math errors / total * 100 as error_rate
```

5) Поиск подозрительных попыток входа (анализ аномалий):

```
_time:1h "failed login" | stats by (user, ip) count() as attempts | filter attempts:>20
```

