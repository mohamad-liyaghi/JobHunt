# JobHunt

## Project Overview

**JobHunt** is a microservice-based project that enables users to authenticate and manage posts. It's designed with a modular architecture to handle specific functionalities efficiently.

### Project Services:

1. **Users Service**
2. **Posts Service**

---

## Users Service

### Overview:

The Users Service is responsible for user authentication, profile management, and data retrieval.
It uses Repository pattern to separate the business logic from the data access logic.

### Technology Stack:

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migration Tool**: Alembic
- **Authentication**: JWT


### Key Features:

- User Registration
- User Login
- Profile Management

---

## Posts Service

### Overview:

The Posts Service is responsible for managing the creation, retrieval, updating, and deletion of user-generated posts.
<br>
It uses MVC as the architectural pattern.

### Technology Stack:

- **Language**: Golang
- **Framework**: Fiber
- **Database**: PostgreSQL
- **ORM**: GORM
- **Migration Tool**: GORM

### Key Features:

- Authentication Middleware
- Create Posts
- Get Posts
- Update Posts
- Delete Posts


---

## Running the Project

You can run each service using Docker or Kubernetes.
<br> First, you need to clone the repository and navigate to the service directory.


1. Clone the repository:
    ```bash
    git clone https://github.com/mohamad-liyaghi/JobHunt.git
    ```

2. Navigate to the directory:
    ```bash
    cd JobHunt/
    ```

### Run Using Docker:

1. Navigate to the service directory:
    ```bash
    cd services/<service_name>/  # Replace <service_name> with 'users' or 'posts'
    ```
2. Build the Docker image:
    ```bash
    make build
   ```

3. Run the service:
    ```bash
    make run
    ```

### Kubernetes:

1. To Deploy the services on Kubernetes, you need to have a Kubernetes cluster running.

2. Run deploy command:
    ```bash
    make deploy
    ```
   
---