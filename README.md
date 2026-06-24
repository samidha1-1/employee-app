# Employee Management System using Docker & MySQL

## Project Overview

This project is a simple Employee Management System built using Flask and MySQL. The application allows users to add, view, and delete employee records. The entire application is containerized using Docker and managed using Docker Compose.

---

## Architecture

```text
Browser
   |
   v
Flask Application Container
   |
   v
MySQL Database Container
```

Both containers communicate through the Docker network created by Docker Compose.

---

## Technologies Used

- Python
- Flask
- MySQL
- Docker
- Docker Compose

---

## Project Structure

```text
employee-app/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
└── templates/
    └── index.html
```

---

## Features

- Add Employee
- View Employee Records
- Delete Employee Records
- MySQL Database Integration
- Dockerized Application
- Multi-Container Deployment using Docker Compose

---

## Docker Concepts Practiced

- Dockerfile
- Docker Images
- Docker Containers
- Docker Networking
- Docker Compose
- Docker Volumes
- Multi-Container Applications

---

## How to Run the Project

### Clone the Repository

```bash
git clone <repository-url>
cd employee-app
```

### Build and Start the Application

```bash
docker compose up --build
```

### Access the Application

Open your browser and visit:

```text
http://localhost:5000
```

---

## Database Access

### Enter the MySQL Container

```bash
docker exec -it <mysql-container-name> bash
```

### Login to MySQL

```bash
mysql -u root -p
```

Enter the password:

```text
root
```

### Show Databases

```sql
SHOW DATABASES;
```

### Use the Employee Database

```sql
USE employee_db;
```

### View Employee Records

```sql
SELECT * FROM employees;
```

---

## How Containers Communicate

The Flask application and MySQL database run in separate containers. Docker Compose automatically creates a network and provides DNS-based service discovery.

The Flask application connects to MySQL using:

```python
host="db"
```

instead of:

```python
host="localhost"
```

because each container has its own localhost. The service name `db` allows Flask to reach the MySQL container over the Docker network.

---

## Challenges Faced

### Port Conflict

Initially, MySQL failed to start because port 3306 was already being used by a MySQL service running on the host machine.

**Solution:**

Changed the port mapping from:

```yaml
3306:3306
```

to:

```yaml
3307:3306
```

---

### MySQL Environment Variables

The MySQL container initially failed because the required root password was not configured.

**Solution:**

Added:

```yaml
MYSQL_ROOT_PASSWORD: root
```

to the Docker Compose file.

---

## Key Learning Outcomes

Through this project, I learned:

- How to containerize a Flask application using Docker.
- How to build custom Docker images.
- How to manage multiple containers using Docker Compose.
- How Docker networking works.
- How containers communicate using service names.
- How to persist MySQL data using Docker Volumes.
- Basic troubleshooting of Docker and MySQL issues.

---

## Future Improvements

- Update Employee Functionality
- Employee Search Feature
- User Authentication
- Jenkins CI/CD Integration
- Kubernetes Deployment
- AWS Deployment

---

## Author

**Samidha Nitin Wani**

DevOps Enthusiast | Linux | Docker | Jenkins | Terraform | Kubernetes (Learning)
