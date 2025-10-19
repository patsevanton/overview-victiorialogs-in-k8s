### Cert-Manager Installation

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.19.1 \
  --set installCRDs=true
```

Apply the ClusterIssuer:
```bash
kubectl apply -f cluster-issuer.yaml
```


helm repo add vm https://victoriametrics.github.io/helm-charts/
helm repo update
kubectl create ns victorialogs
helm upgrade --install vlc vm/victoria-logs-cluster -n victorialogs -f victorialogs-cluster-values.yaml

kubectl apply -f nginx-log-generator.yaml

kubectl create ns victoria-metrics
helm upgrade --install victoria-metrics vm/victoria-metrics-cluster -f vmks-values.yaml -n victoria-metrics

kubectl apply -f prometheus-metrics-generator.yaml

docker build -t antonpatsev/log-generator:2 .
docker push antonpatsev/log-generator:2
kubectl apply -f python-log-generator.yaml


### WordPress Installation

```bash
helm upgrade --install my-wordpress-release oci://registry-1.docker.io/bitnamicharts/wordpress \
  --set ingress.enabled=true \
  --set ingress.hostname=wordpress.apatsev.org.ru \
  --set ingress.ingressClassName=nginx \
  --set-json ingress.annotations='{"cert-manager.io/cluster-issuer":"letsencrypt-prod"}' \
  --set ingress.tls=true
```


### Generating Attack Logs

To simulate attacks and generate corresponding logs, you can use the following tools.

**Disclaimer:** Only use these tools on systems you have explicit permission to test.


**2. Web Directory Brute-forcing with gobuster**

```bash
gobuster dir -u https://wordpress.apatsev.org.ru -w /home/user/github/danielmiessler/SecLists-master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt
```

**3. Login Brute-forcing with Hydra**

```bash
hydra -L /home/user/github/danielmiessler/SecLists-master/Usernames/xato-net-10-million-usernames.txt -P /home/user/github/danielmiessler/SecLists-master/Passwords/Common-Credentials/Pwdb_top-10000000.txt wordpress.apatsev.org.ru https-post-form "/login.php:username=^USER^&password=^PASS^:F=Invalid"
```

**4. Vulnerability Scanning with Nikto**

```bash
nikto -h https://wordpress.apatsev.org.ru
```

