# Deploying the flask api server in Minikube

The flask-api is a python package which jumbles the word and audits the last 10 api calls.

## Installation

Download the package locally from the git

```
https://github.com/ragavendranps/flask-api
```
Install minikube and helm on your local machine:
```
● https://minikube.sigs.k8s.io/docs/start/
● https://helm.sh/docs/intro/install/
```

## Usage

The python file is containerised and the image is pushed to docker hub in the repository ragps/flask-api 

Deployment templates for the api server are updated using Helm. Use the below commands to install.

``` 
helm install <release_name> <chart_name> 
```

This will deploy the api-server and its service in minikube. This can be verified using the command 

```
kubectl get deployments
kubectl get service
```
Since the service is configured via NodePort, the application can be browsed with <nodeip>:<nodeport>

