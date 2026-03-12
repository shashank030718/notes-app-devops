"# Notes App DevOps Project" 
# 📝 Notes App — DevOps Project

A production-grade 3-tier containerized application deployed on AWS using modern DevOps practices.

## 🏗️ Architecture
- **Frontend**: Nginx serving static HTML
- **Backend**: Python Flask REST API
- **Database**: PostgreSQL (AWS RDS)
- **Container Registry**: AWS ECR
- **Container Orchestration**: AWS ECS Fargate
- **Infrastructure as Code**: Terraform
- **CI/CD**: GitHub Actions

## 🔄 CI/CD Pipeline
Every push to `main` branch automatically:
1. Builds Docker images
2. Pushes to AWS ECR
3. Forces ECS redeployment
4. Waits for stable deployment

## 🛠️ Tech Stack
`Docker` `Terraform` `AWS ECS` `AWS ECR` `AWS RDS` `GitHub Actions` `Python Flask` `PostgreSQL` `Nginx`

## 🚀 Local Setup
```bash
git clone https://github.com/shashank030718/notes-app-devops.git
cd notes-app-devops
docker-compose up --build
```
Open http://localhost:8080

## ☁️ Infrastructure
Provisioned with Terraform:
- VPC with public/private subnets across 2 AZs
- ECS Fargate cluster (serverless containers)
- RDS PostgreSQL (managed database)
- ECR repositories for Docker images
- CloudWatch logging
- IAM roles with least-privilege policies
