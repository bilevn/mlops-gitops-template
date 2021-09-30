# MLOps GitOps Template
*Work in progress...*
# Infrastructure setup
## Cluster base infrastructure
Get kind ([ref](https://kind.sigs.k8s.io/docs/user/quick-start/)):
```bash
brew install kind
```
___
Get kubectl ([ref](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)):
```bash
brew install kubectl 
```
___
Get helm ([ref](https://helm.sh/docs/intro/install/)):
```bash
brew install helm
```
___
Create kind cluster:
```bash
kind create cluster
```
___
Get istio ([ref](https://istio.io/latest/docs/setup/getting-started/)):
```bash
curl -L https://istio.io/downloadIstio | sh -

cd istio-1.11.3

export PATH=$PWD/bin:$PATH
istioctl install --set profile=demo -y

kubectl label namespace default istio-injection=enabled
```
> Folow the actual instructions on the webside

## Seldon Core
Create namespaces ([ref](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html)):
```bash
kubectl create namespace seldon-system
kubectl create namespace seldon
```
___
Enable istio in the namespaces:
```bash
kubectl label namespace seldon-system istio-injection=enabled
kubectl label namespace seldon istio-injection=enabled
```
___
Install the platform using helm ([ref](https://docs.seldon.io/projects/seldon-core/en/latest/workflow/github-readme.html)):
```bash
helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --namespace seldon-system \
    --set istio.enabled=true
```
___
Create istio gareway for seldon projects ([ref](https://github.com/SeldonIO/seldon-core/blob/master/doc/source/ingress/istio.md)):
```bash
kubectl apply -f ./infra/seldon/istio-gateway.yaml
```
___
Port-forward istio gateway ingress:
```bash
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```
> Additional resource for referencing: [ref](https://docs.seldon.io/projects/seldon-core/en/v1.9.1/examples/istio_examples.html)

# Development
Install requirements:
```bash
pip install -r requirements/production.txt -r requirements/development.txt
```

Get example data:
```bash
bash get_data.sh
```

Formatter:
```bash
black .
```

Type checking:
```bash
mypy models
```

Testing:
```bash
python -m pytest --cov=models
```

Validate model:
```bash
python -m models validate
```

Train model:
```bash
python -m models train --id test
```