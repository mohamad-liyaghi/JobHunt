# JobHunt Users Service

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies](#technologies)
3. [Overview](#overview)
4. [How to Run](#how-to-run)

## Introduction <a name="introduction"></a>
The JobHunt Users service is responsible for managing user registration and related functionalities within the JobHunt platform. This service is built using FastAPI and utilizes PostgreSQL as its database. Alembic is used for database migrations, and the service follows the repository pattern for its architecture.

This documentation provides an overview of the JobHunt Users service, including the technologies used, an overview of the service, and instructions on how to run the service locally or deploy it using Kubernetes.

## Technologies <a name="technologies"></a>
The JobHunt Users service utilizes the following technologies:
1. FastAPI
2. PostgreSQL
3. Alembic
4. Kubernetes
5. Docker

## Overview <a name="overview"></a>
The Users service is responsible for managing user registration and related functionalities. It follows the repository pattern, ensuring a clear separation of concerns and maintainability.

## How to Run <a name="how-to-run"></a>
To run the Users service of the JobHunt project, follow the steps below:


1. First, clone the project repository:
    ```bash
    git clone https://github.com/mohamad-liyaghi/JobHunt.git
    ```

2. Navigate to the Users service directory:
    ```bash
    cd JobHunt/services/users/ 
    ```

### Run on Kubernetes:
1. Create ConfigMaps for environment variables:
    ```bash
    make create-confmap
    ```

2. Apply Kubernetes deployments:
    ```bash
    kubectl apply -f ../../k8s/users
    ```

### Run via Docker:
1. First, navigate to the Users service directory:
    ```bash
    cd JobHunt/services/users
    ```

2. Build the Docker image:
    ```bash
    make build
    ```

3. Run the Docker container:
    ```bash
      make run DETACHED=true
    ```

4. Run Tests:
    ```bash
    make test
   ```

Now The Users service should be up and running. You can access the service at `http://localhost:8000`.
