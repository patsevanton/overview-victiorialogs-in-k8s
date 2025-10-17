helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster -n victorialogs -f victorialogs-cluster-values.yaml


kubectl apply -f flog1.yaml
kubectl apply -f flog2.yaml
