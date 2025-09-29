# ElevateLab_Task5-K8S-minikube-
Task 5: Deploy Python Flask App on Minikube Kubernetes

         Overview
This project demonstrates deploying a simple Python Flask application on a local Kubernetes cluster using Minikube
It covers building a Docker image, creating Kubernetes Deployment and Service, scaling pods, and accessing the application.



## Project Structure
ElevateLab_Task5-K8S-minikube/
│
├── app.py # Flask application

├── requirements.txt # Python dependencies

├── Dockerfile # Dockerfile for building the app image

├── deployment.yml # Kubernetes Deployment manifest

├── service.yml # Kubernetes Service manifest

└── README.md #Documentation

└──SCREENSHOTS #for proof



## Prerequisites
- Docker
- Minikube
- kubectl
- Python 3



## Steps to Run Locally in Docker

1. Build Docker image:

        docker build -t flask-app:1.0 .
Run container:

        docker run -d -p 4000:4000 flask-app:1.0
Open in browser:

        http://localhost:4000
        
Deploy on Minikube Kubernetes

Start Minikube:

    minikube start --driver=docker
    eval $(minikube docker-env)
    
Build Docker image inside Minikube:

    docker build -t flask-app:1.0 .
    
Apply Deployment and Service:

    kubectl apply -f deployment.yml
    kubectl apply -f service.yml
    
Verify pods and service:

    kubectl get pods
    kubectl get svc
    
Access the app:

    minikube service flask-app-service
    
Scale the Deployment:


    kubectl scale deployment flask-app-deployment --replicas=4
    kubectl get pods
    
Kubernetes automatically creates new pods to match the desired replica count.

Notes
Flask app runs on port 4000, which is exposed via NodePort 30008 in Kubernetes.

Use kubectl logs <pod-name> and kubectl describe pod <pod-name> to debug pods.

Output:

Hands-on experience with Kubernetes Deployments, Services, scaling, and pod management.

Demonstrates end-to-end workflow from Docker container → Minikube cluster → Kubernetes deployment.


