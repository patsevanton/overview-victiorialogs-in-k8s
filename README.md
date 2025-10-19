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

kubectl apply -f python-log-generator.yaml

### Generating Attack Logs

To simulate attacks and generate corresponding logs, you can use the following tools.

**Disclaimer:** Only use these tools on systems you have explicit permission to test.

**1. Port Scanning with Nmap**

```bash
nmap -sV -p- <target-ip>
```

**2. Web Directory Brute-forcing with gobuster**

```bash
gobuster dir -u http://<target-ip> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

**3. Login Brute-forcing with Hydra**

```bash
hydra -L users.txt -P passwords.txt <target-ip> http-post-form "/login.php:username=^USER^&password=^PASS^:F=Invalid"
```

**4. Vulnerability Scanning with Nikto**

```bash
nikto -h http://<target-ip>
```