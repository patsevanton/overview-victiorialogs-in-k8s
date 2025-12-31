# Установка k8s-event-logger
```bash
helm upgrade --install k8s-event-logger \
  oci://ghcr.io/deliveryhero/helm-charts/k8s-event-logger \
  --namespace k8s-event-logger \
  --create-namespace \
  --wait \
  --version 1.1.10 \
  --timeout 15m
```

# Установка eventrouter
```
helm repo add wikimedia https://helm-charts.wikimedia.org/stable/
helm install my-eventrouter wikimedia/eventrouter --version 0.4.4
```


### Stress
```bash
kubectl create ns stress1
kubectl apply -f stress1.yaml

kubectl create ns stress2
kubectl apply -f stress2.yaml

kubectl create ns stress3
kubectl apply -f stress3.yaml
```
