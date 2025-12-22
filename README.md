# Overview: VictoriaLogs in Kubernetes

## Введение

**VictoriaLogs** — это высокопроизводительное хранилище логов от команды VictoriaMetrics, оптимизированное под большие объёмы данных, низкое потребление ресурсов и простоту эксплуатации. В Kubernetes VictoriaLogs органично вписывается в экосистему observability и может использоваться как централизованное лог-хранилище для приложений, ingress-контроллеров и security-событий.

В этой статье мы рассмотрим:

* архитектуру VictoriaLogs в Kubernetes,
* установку через Helm,
* интеграцию с cert-manager и ingress,
* генерацию логов и метрик,
* пример практического сценария с WordPress и эмуляцией атак.

## Архитектура решения

В рамках Kubernetes-кластера разворачиваются следующие компоненты:

* **cert-manager** — автоматическое управление TLS-сертификатами (Let’s Encrypt)
* **VictoriaLogs Cluster** — распределённое хранилище логов
* **Victoria Metrics K8s Stack** — сбор метрик (Prometheus-совместимый стек)
* **Log Generators** — генераторы логов (nginx, python-приложения)
* **Ingress Controller (nginx)** — источник access/error логов
* **WordPress** — реальное приложение для генерации пользовательских и security-событий

Такой стек позволяет не только хранить логи, но и коррелировать их с метриками и событиями безопасности.

## Установка cert-manager

Для работы ingress с TLS используется cert-manager.

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.19.2 \
  --wait \
  --set crds.enabled=true
```

После установки применяется `ClusterIssuer`, который будет использоваться ingress-ресурсами для автоматического выпуска сертификатов:

```bash
kubectl apply -f cluster-issuer.yaml
```

## Развёртывание VictoriaLogs Cluster

VictoriaLogs устанавливается через официальный Helm-репозиторий VictoriaMetrics.

```bash
helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update

kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster \
  -n victorialogs \
  --wait \
  --version 0.0.21 \
  -f victorialogs-cluster-values.yaml
```

### Почему кластерный режим?

* горизонтальное масштабирование
* отказоустойчивость
* высокая скорость записи логов
* подходит для production-нагрузок

## Генерация логов

Для демонстрации и тестирования используются несколько источников логов.

### NGINX Log Generator

```bash
kubectl apply -f nginx-log-generator.yaml
```

Генерирует HTTP access-логи, близкие к реальным ingress-сценариям.

### Python Log Generator

Сборка и публикация Docker-образа:

```bash
docker build -t antonpatsev/log-generator:2 .
docker push antonpatsev/log-generator:2
kubectl apply -f python-log-generator.yaml
```

Позволяет эмулировать application-level логи (INFO, WARN, ERROR).

Открываем https://victorialogs.apatsev.org.ru/select/vmui и смотрим

* всплески 4xx/5xx,
* аномальные паттерны запросов,
* сигнатуры атак в логах ingress и приложения.

## Практическая ценность VictoriaLogs

VictoriaLogs в Kubernetes позволяет:

* централизованно хранить логи без Elasticsearch
* обрабатывать миллионы строк в секунду
* быстро выполнять search и filtering
* эффективно работать с security-логами
* коррелировать логи с метриками VictoriaMetrics

В сочетании с реальными сценариями (WordPress + атаки) это делает VictoriaLogs отличной основой для:

* observability,
* troubleshooting,
* security monitoring,
* SOC / SIEM-like use cases.

## Мониторинг: Victoria Metrics K8s Stack

Для мониторинга инфраструктуры разворачивается Victoria Metrics K8s Stack.

```bash
kubectl create ns vmks
helm upgrade --install vmks vm/victoria-metrics-k8s-stack \
  -n vmks \
  --wait \
  --version 0.66.0 \
  -f vmks-values.yaml
```

Открываем https://grafana.apatsev.org.ru/ и смотрим нагрузку на систему

## Заключение

VictoriaLogs — зрелое и production-ready решение для логирования в Kubernetes. Простота установки через Helm, высокая производительность и нативная интеграция с экосистемой VictoriaMetrics делают его отличной альтернативой тяжёлым ELK-стекам, особенно в cloud-native средах.
