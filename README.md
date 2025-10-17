helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster -n victorialogs -f victorialogs-cluster-values.yaml


helm repo add kube-logging https://kube-logging.github.io/helm-charts
helm install --generate-name --wait kube-logging/log-generator

kubectl create ns victoria-metrics
helm upgrade --install victoria-metrics vm/victoria-metrics-cluster -f vmks-values.yaml -n victoria-metrics