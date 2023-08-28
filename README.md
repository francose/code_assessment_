# Terraform AWS ECS Deployment Documentation

## Introduction

This documentation provides an overview of deploying a Docker containerized application to AWS ECS using Fargate with the help of Terraform.

## Table of Contents

1. [Terraform Configuration Structure](#terraform-configuration-structure)
2. [Required AWS Services and Resources](#required-aws-services-and-resources)
3. [Troubleshooting Common ECS Deployment Issues](#troubleshooting-common-ecs-deployment-issues)
4. [Resolving Docker Image Architecture Mismatch](#resolving-docker-image-architecture-mismatch)

---

## Terraform Configuration Structure

- **Providers**: Define cloud providers and versions. In this context, we used the AWS provider.
- **Variables**: Store sensitive data, such as AWS `access_key` and `secret_key`, to avoid hardcoding them.
- **Resources**: Define the AWS resources like ECS cluster, task definitions, security groups, IAM roles, etc.
- **Outputs**: Display essential information after Terraform applies, like the application's URL.

---

## Required AWS Services and Resources

- **ECR (Elastic Container Registry)**: Used to store Docker images.
- **ECS (Elastic Container Service)**: Used to run Docker containers.
  - Fargate launch type abstracts underlying EC2 instances.
- **ALB (Application Load Balancer)**: Directs traffic to the containers.
- **IAM**: Define roles and permissions for ECS tasks.
- **VPC, Subnets, and Security Groups**: Network configurations to secure and route traffic.

---

## Troubleshooting Common ECS Deployment Issues

- **Task Definition & Image**: Ensure the Docker image is available in ECR and starts a persistent process.
- **Resource Allocation**: Ensure sufficient CPU and memory.
- **Networking & Security Groups**: Ensure tasks can pull Docker images and communicate with other services.
- **Task Role & Execution Role**: Ensure necessary permissions for tasks.
- **Logs**: Use AWS Log Driver to send container logs to CloudWatch.
- **Health Checks**: Ensure the container application responds correctly to health checks.
- **VPC & Subnets**: Ensure the network is set up correctly.
- **Dependencies**: Ensure the container can connect to required services.
- **Task Start Time**: Ensure the application starts within the ECS start timeout.

---

## Resolving Docker Image Architecture Mismatch

A common issue when deploying Docker containers to cloud environments is an architecture mismatch between the built image and the target environment.

**Symptom**: CloudWatch logs display "exec format error".

**Solution**:

1. **Check Docker Image Architecture**: Use `docker image inspect <image_name>` to verify the architecture.
2. **Rebuild for the Correct Architecture**: Use Docker's `buildx` command to target the correct architecture. For example:
   ```bash
   docker buildx build --platform=linux/amd64 -t <image-name>
   ```

# Results:

After all here is the [react app](http://load-balancer-dev-1842764609.us-east-1.elb.amazonaws.com)
