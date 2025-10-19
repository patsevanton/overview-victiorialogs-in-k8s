helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster -n victorialogs -f victorialogs-cluster-values.yaml

kubectl apply -f nginx-log-generator.yaml
kubectl apply -f nginx-log-generator2.yaml

kubectl create ns victoria-metrics
helm upgrade --install victoria-metrics vm/victoria-metrics-cluster -f vmks-values.yaml -n victoria-metrics

kubectl apply -f prometheus-metrics-generator.yaml
docker login

docker build -t antonpatsev/log-generator:2 .

docker push antonpatsev/log-generator:2

kubectl apply -f log-generator.yaml
