# 🚀 DevOps Notes – Complete Learning Guide

![DevOps](https://img.shields.io/badge/DevOps-Learning-blue)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform&logoColor=white)

Welcome to my DevOps Notes repository! This repository contains technical notes, practical commands, configuration examples, scripts, screenshots, and learning resources related to DevOps, Cloud Computing, Linux, Networking, Docker, Kubernetes, Jenkins, Terraform, AWS, and monitoring.

The goal is to build practical DevOps knowledge through hands-on exercises and real-world projects.

---

# 📚 Table of Contents

1. [DevOps Fundamentals](#1-devops-fundamentals)
2. [Linux Commands](#2-linux-commands)
3. [Shell Scripting](#3-shell-scripting)
4. [Git and GitHub](#4-git-and-github)
5. [Networking Fundamentals](#5-networking-fundamentals)
6. [AWS Cloud Computing](#6-aws-cloud-computing)
7. [Docker](#7-docker)
8. [Kubernetes](#8-kubernetes)
9. [Jenkins and CI/CD](#9-jenkins-and-cicd)
10. [Terraform](#10-terraform)
11. [Monitoring with Prometheus and Grafana](#11-monitoring-with-prometheus-and-grafana)
12. [Python Scripting](#12-python-scripting)
13. [HTML and Dockerfile](#13-html-and-dockerfile)
14. [DevOps Project Workflow](#14-devops-project-workflow)
15. [Troubleshooting Commands](#15-troubleshooting-commands)
16. [Repository Structure](#16-repository-structure)
17. [Learning Roadmap](#17-learning-roadmap)
18. [Author](#18-author)

---

# 1. DevOps Fundamentals

## What is DevOps?

DevOps combines development (Dev) and operations (Ops) practices to improve software delivery, automation, collaboration, reliability, and deployment speed.

### Benefits of DevOps

- Faster software delivery.
- Automated testing and deployment.
- Improved collaboration between teams.
- Consistent application environments.
- Better monitoring and troubleshooting.
- More reliable infrastructure management.

## DevOps Lifecycle

```text
Plan
  |
  v
Code
  |
  v
Build
  |
  v
Test
  |
  v
Release
  |
  v
Deploy
  |
  v
Operate
  |
  v
Monitor
  |
  +----------> Feedback and improvement
```

## Common DevOps Tools

| Category | Tools |
|---|---|
| Version Control | Git, GitHub |
| Operating Systems | Linux, Ubuntu |
| Cloud Computing | AWS |
| Containerization | Docker |
| Container Orchestration | Kubernetes |
| CI/CD | Jenkins |
| Infrastructure as Code | Terraform |
| Configuration Management | Ansible |
| Monitoring | Prometheus, Grafana |
| Logging | Loki, Promtail |
| GitOps | Argo CD |
| Scripting | Bash, Python |

---

# 2. Linux Commands

Linux is widely used for servers, cloud infrastructure, containers, and DevOps automation.

## File and Directory Commands

| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls` | List files |
| `ls -la` | List all files with details |
| `cd /path` | Change directory |
| `mkdir project` | Create a directory |
| `touch file.txt` | Create an empty file |
| `cat file.txt` | Display file contents |
| `less file.txt` | Read a file page by page |
| `cp file.txt backup.txt` | Copy a file |
| `mv old.txt new.txt` | Move or rename a file |
| `rm file.txt` | Delete a file |
| `find . -name "*.tf"` | Find Terraform files |

## System Monitoring

```bash
uptime
free -h
df -h
du -sh .
top
ps aux
```

## Process Management

```bash
ps aux
pgrep nginx
kill <PID>
```

Use `kill -9 <PID>` only when normal termination does not work and forced termination is appropriate.

## Permissions

```bash
ls -l
chmod 644 file.txt
chmod 755 script.sh
```

Make a script executable:

```bash
chmod +x script.sh
```

## Services

On systemd-based Linux distributions:

```bash
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
```

## Networking Commands

```bash
ip addr
ip route
ping 8.8.8.8
curl -I https://example.com
ss -tulpn
```

---

# 3. Shell Scripting

Shell scripting automates repetitive system administration and DevOps tasks.

## Example 1: Hello World

```bash
#!/bin/bash

echo "Hello, DevOps!"
```

Run:

```bash
chmod +x hello.sh
./hello.sh
```

## Example 2: Variables

```bash
#!/bin/bash

NAME="Shubham"

echo "Welcome, $NAME"
```

## Example 3: If-Else

```bash
#!/bin/bash

NUMBER=10

if [ "$NUMBER" -gt 5 ]; then
    echo "Number is greater than 5"
else
    echo "Number is 5 or less"
fi
```

## Example 4: For Loop

```bash
#!/bin/bash

for i in 1 2 3 4 5
do
    echo "Number: $i"
done
```

## Example 5: While Loop

```bash
#!/bin/bash

COUNT=1

while [ "$COUNT" -le 5 ]
do
    echo "$COUNT"
    COUNT=$((COUNT + 1))
done
```

## Example 6: Check a Service

```bash
#!/bin/bash

if systemctl is-active --quiet nginx; then
    echo "Nginx is running"
else
    echo "Nginx is not running"
fi
```

## Example 7: Check Disk Usage

```bash
#!/bin/bash

df -h
```

---

# 4. Git and GitHub

Git is a distributed version control system. GitHub hosts Git repositories and supports collaboration.

## Common Git Commands

| Command | Purpose |
|---|---|
| `git init` | Initialize a repository |
| `git clone <URL>` | Clone a repository |
| `git status` | Check working tree status |
| `git add .` | Stage changes |
| `git add README.md` | Stage a specific file |
| `git commit -m "message"` | Commit staged changes |
| `git log --oneline` | Show commit history |
| `git branch` | List branches |
| `git switch -c feature` | Create and switch to a branch |
| `git pull` | Fetch and integrate remote changes |
| `git push` | Push commits |
| `git remote -v` | Display remote URLs |

## Upload a Project to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_REPOSITORY_URL` with your repository URL.

If `origin` already exists, update it instead of adding it again:

```bash
git remote set-url origin YOUR_REPOSITORY_URL
```

## Example `.gitignore`

```gitignore
node_modules/
.terraform/
*.tfstate
*.tfstate.*
.env
.env.*
!.env.example
__pycache__/
*.pyc
.DS_Store
Thumbs.db
```

**Important:** Review your ignore rules before committing. Keep Terraform provider lock files such as `.terraform.lock.hcl` in Git. Never commit credentials, private SSH keys, or real secret values.

---

# 5. Networking Fundamentals

Networking knowledge is essential for cloud computing and DevOps.

## Common Networking Concepts

| Concept | Explanation |
|---|---|
| IP Address | Identifies a network interface |
| Subnet | Divides a network into smaller networks |
| DNS | Resolves domain names to IP addresses |
| DHCP | Automatically assigns network configuration |
| NAT | Translates network addresses |
| Firewall | Controls network traffic |
| Router | Forwards packets between networks |
| Switch | Connects devices within a network |
| TCP | Reliable, connection-oriented transport |
| UDP | Connectionless transport |
| ICMP | Used for network diagnostics and error reporting |
| HTTP | Application protocol for web communication |
| HTTPS | HTTP secured using TLS |

## Common Ports

| Port | Service |
|---|---|
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 3000 | Common development application port |
| 5000 | Common development/API port |
| 8080 | Common alternate HTTP/application port |
| 9090 | Default Prometheus web port |

Ports may differ depending on application configuration.

## Useful Commands

```bash
ip addr
ip route
nslookup example.com
dig example.com
ping example.com
traceroute example.com
curl -I https://example.com
ss -tulpn
```

---

# 6. AWS Cloud Computing

Amazon Web Services provides on-demand cloud infrastructure and managed services.

## Important AWS Services

| Service | Purpose |
|---|---|
| EC2 | Virtual servers |
| S3 | Object storage |
| IAM | Identity and access management |
| VPC | Virtual private networking |
| ELB | Load balancing |
| Auto Scaling | Adjust instance capacity |
| Route 53 | DNS and domain routing |
| CloudWatch | Monitoring and logs |
| ECR | Container image registry |
| ECS | Container orchestration |
| EKS | Managed Kubernetes |
| Lambda | Serverless compute |
| RDS | Managed relational databases |

## EC2 Deployment Workflow

```text
Create VPC
   |
   v
Configure Subnet and Routing
   |
   v
Configure Security Group
   |
   v
Launch EC2 Instance
   |
   v
Connect Using SSH or SSM
   |
   v
Install and Run Application
   |
   v
Monitor with CloudWatch
```

## AWS CLI Commands

Check AWS identity:

```bash
aws sts get-caller-identity
```

List EC2 instances:

```bash
aws ec2 describe-instances
```

List S3 buckets:

```bash
aws s3 ls
```

List configured AWS regions:

```bash
aws ec2 describe-regions --output table
```

## AWS Security Best Practices

- Follow least-privilege IAM permissions.
- Prefer IAM roles and temporary credentials.
- Restrict security group access.
- Avoid exposing SSH or database ports publicly.
- Enable monitoring and logging.
- Protect access keys and private keys.
- Review costs and remove unused resources.

---

# 7. Docker

Docker packages applications and their dependencies into containers.

## Important Docker Commands

| Command | Purpose |
|---|---|
| `docker --version` | Show Docker version |
| `docker images` | List images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker pull nginx` | Pull an image |
| `docker build -t app:1.0 .` | Build an image |
| `docker run -d -p 8080:80 nginx` | Run a container |
| `docker logs <container>` | View container logs |
| `docker exec -it <container> sh` | Open a shell |
| `docker stop <container>` | Stop a container |
| `docker rm <container>` | Remove a container |
| `docker rmi <image>` | Remove an image |

## Example Dockerfile

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

This is an example for a Node.js application whose `package.json` defines a suitable `start` script.

## Build and Run

```bash
docker build -t my-app:1.0 .
docker run -d --name my-app -p 3000:3000 my-app:1.0
docker logs my-app
```

Open the application at:

`http://localhost:3000`

## Docker Compose

Start services:

```bash
docker compose up -d
```

List services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop services:

```bash
docker compose down
```

---

# 8. Kubernetes

Kubernetes orchestrates containers across a cluster of machines.

## Kubernetes Architecture

```text
                CONTROL PLANE
        +--------------------------+
        | API Server               |
        | Scheduler                |
        | Controller Manager       |
        | etcd                     |
        +--------------------------+
                    |
                    v
                WORKER NODES
        +--------------------------+
        | Kubelet                  |
        | Container Runtime        |
        | Pods                     |
        +--------------------------+
```

## Important Kubernetes Resources

| Resource | Purpose |
|---|---|
| Pod | Runs one or more containers |
| Deployment | Manages replicated Pods |
| Service | Provides stable network access to Pods |
| ConfigMap | Stores non-sensitive configuration |
| Secret | Stores sensitive configuration data |
| Namespace | Separates resources logically |
| Ingress | Manages HTTP/HTTPS routing into a cluster |
| DaemonSet | Runs a Pod on selected nodes |
| StatefulSet | Manages stateful applications |
| Job | Runs a task to completion |
| CronJob | Runs scheduled Jobs |
| HPA | Automatically scales replica count |

## Common Kubernetes Commands

```bash
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get all
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl apply -f deployment.yaml
kubectl delete -f deployment.yaml
```

## Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:stable
          ports:
            - containerPort: 80
```

Apply the configuration:

```bash
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods
```

## Service Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

Apply:

```bash
kubectl apply -f service.yaml
kubectl get services
```

## Scaling a Deployment

```bash
kubectl scale deployment nginx-deployment --replicas=5
```

## Horizontal Pod Autoscaler

```bash
kubectl autoscale deployment nginx-deployment --min=2 --max=10 --cpu-percent=70
```

HPA requires suitable metrics to be available, typically through Metrics Server for CPU-based scaling.

---

# 9. Jenkins and CI/CD

Jenkins automates build, test, and deployment workflows.

## CI/CD Pipeline

```text
Developer Pushes Code
         |
         v
      GitHub
         |
         v
      Jenkins
         |
         v
     Build Image
         |
         v
      Run Tests
         |
         v
 Push Image to Registry
         |
         v
 Deploy to Kubernetes
         |
         v
 Verify and Monitor
```

## Jenkins Pipeline Example

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build application'
            }
        }

        stage('Test') {
            steps {
                echo 'Run automated tests'
            }
        }

        stage('Package') {
            steps {
                echo 'Package application'
            }
        }
    }
}
```

This is a starter pipeline. Add project-specific build, test, image publishing, and deployment commands before using it for production.

## Jenkins Best Practices

- Store pipeline definitions in a `Jenkinsfile`.
- Use Jenkins credentials for secrets.
- Avoid hardcoding passwords and tokens.
- Run automated tests before deployment.
- Restrict production deployment permissions.
- Keep build logs and monitor pipeline failures.

---

# 10. Terraform

Terraform is an Infrastructure as Code tool used to provision and manage infrastructure.

## Terraform Workflow

```text
Write Configuration
        |
        v
terraform init
        |
        v
terraform fmt
        |
        v
terraform validate
        |
        v
terraform plan
        |
        v
terraform apply
        |
        v
Manage Infrastructure
```

## Example AWS Provider Configuration

```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
```

This example uses the Mumbai AWS region. Change the region to the one appropriate for your project.

## Terraform Commands

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform output
terraform state list
terraform destroy
```

## Terraform Best Practices

- Use variables instead of hardcoding reusable values.
- Review `terraform plan` before applying changes.
- Keep `.terraform.lock.hcl` under version control.
- Exclude the `.terraform/` working directory from Git.
- Never commit real secrets or sensitive state files.
- Use remote state and state locking when appropriate for team projects.
- Back up state and restrict access to it.

---

# 11. Monitoring with Prometheus and Grafana

Monitoring helps teams understand application health, infrastructure performance, and service availability.

## Prometheus

Prometheus collects and stores time-series metrics.

Common use cases:

- CPU and memory monitoring.
- Application metrics.
- Alerting rules.
- Kubernetes monitoring.
- Service availability monitoring.

## Grafana

Grafana visualizes metrics using dashboards and panels.

It can connect to Prometheus and other supported data sources.

## Monitoring Architecture

```text
Application / Infrastructure
             |
             v
      Metrics Exporters
             |
             v
         Prometheus
             |
             v
           Grafana
             |
             v
       Dashboards / Alerts
```

## Useful Commands

Check Kubernetes resources:

```bash
kubectl get pods -A
kubectl get services -A
```

Check Prometheus or Grafana Pods by namespace:

```bash
kubectl get pods -n monitoring
```

The namespace may differ depending on your installation.

## Monitoring Best Practices

- Monitor CPU, memory, and disk usage.
- Configure meaningful alerts.
- Track application availability and latency.
- Use dashboards for important services.
- Review logs when metrics indicate a problem.

---

# 12. Python Scripting

Python is useful for automation, file handling, APIs, and operational scripts.

## Example 1: Hello World

```python
print("Hello, DevOps!")
```

## Example 2: Loop

```python
for number in range(1, 6):
    print(number)
```

## Example 3: Read a File

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

## Example 4: Handle Exceptions

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
```

## Example 5: Check Disk Usage on Linux

```python
import shutil

usage = shutil.disk_usage("/")

print(f"Total: {usage.total // (1024**3)} GB")
print(f"Used: {usage.used // (1024**3)} GB")
print(f"Free: {usage.free // (1024**3)} GB")
```

---

# 13. HTML and Dockerfile

HTML defines the structure of web pages. A Dockerfile describes how to build a container image.

## Simple HTML Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Project</title>
</head>
<body>
    <h1>Welcome to My DevOps Project</h1>
    <p>Learning Docker, Kubernetes, AWS, and CI/CD.</p>
</body>
</html>
```

## Dockerfile for a Static HTML Website

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

Build and run:

```bash
docker build -t devops-website:1.0 .
docker run -d -p 8080:80 devops-website:1.0
```

Open:

`http://localhost:8080`

---

# 14. DevOps Project Workflow

A typical DevOps project may follow this workflow:

1. Write application code.
2. Store code in GitHub.
3. Build and test the application.
4. Create a Docker image.
5. Push the image to a container registry.
6. Provision infrastructure using Terraform when required.
7. Deploy the application to Kubernetes or another hosting platform.
8. Automate deployment with Jenkins.
9. Monitor the application with Prometheus and Grafana.
10. Review logs, metrics, alerts, and deployment status.

```text
Code
 |
 v
GitHub
 |
 v
Jenkins CI/CD
 |
 v
Build and Test
 |
 v
Docker Image
 |
 v
Container Registry
 |
 v
Kubernetes
 |
 v
Prometheus and Grafana
```

---

# 15. Troubleshooting Commands

## Linux

```bash
df -h
free -h
uptime
ps aux
systemctl status nginx
journalctl -u nginx
```

## Docker

```bash
docker ps -a
docker images
docker logs <container-name>
docker inspect <container-name>
docker system df
```

## Kubernetes

```bash
kubectl get pods -A
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl get events
kubectl get nodes
```

## Jenkins

Check the Jenkins service on a systemd-based Linux installation:

```bash
sudo systemctl status jenkins
sudo journalctl -u jenkins
```

## Terraform

```bash
terraform fmt
terraform validate
terraform plan
terraform providers
terraform state list
```

## Git

```bash
git status
git log --oneline
git remote -v
git diff
```

---

# 16. Repository Structure

This repository contains notes, scripts, configuration examples, and screenshots.

The files are organized by topic as the repository grows.

Examples of existing resources include:

- Python practice scripts.
- Shell scripts.
- Docker and Dockerfile notes.
- Jenkins pipeline notes.
- Kubernetes and Grafana screenshots.
- Networking and virtualization notes.
- DevOps diagrams and reference images.

Use the repository file list to explore individual examples and screenshots.

---

# 17. Learning Roadmap

Recommended learning sequence:

- [ ] Linux fundamentals and commands
- [ ] Networking fundamentals
- [ ] Git and GitHub
- [ ] Shell scripting
- [ ] Python automation
- [ ] AWS fundamentals
- [ ] Docker and containerization
- [ ] Kubernetes
- [ ] Jenkins and CI/CD
- [ ] Terraform and Infrastructure as Code
- [ ] Prometheus and Grafana
- [ ] Logging and troubleshooting
- [ ] End-to-end DevOps project

---

# 18. Author

**Shubham Dadwal**

GitHub: [@shubhamdadwal1](https://github.com/shubhamdadwal1)

Repository: [devops-notes](https://github.com/shubhamdadwal1/devops-notes)

---

## 📄 License

This repository is intended for educational and learning purposes. Add a `LICENSE` file if you want to distribute the notes under a specific open-source license.

---

⭐ If these notes help you learn DevOps, feel free to explore the repository and practice the examples.
