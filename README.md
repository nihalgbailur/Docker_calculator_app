# Simple Calculator Docker Project

This project demonstrates how to containerize a Python-based simple calculator application using Docker. The containerized application includes basic arithmetic operations (`+`, `-`, `*`, `/`) and logs its output to a file located in `/var/log/calculator.log`.

---

## **Features**

- Simple interactive calculator.
- Logs all user inputs, operations, and errors to `/var/log/calculator.log`.
- Dockerized for portability and ease of deployment.
- Health checks to monitor container status.

---

## **File Structure**

```
.
├── app
│   ├── calculator.py        # Main Python script for the calculator
│   ├── entrypoint.sh        # Entrypoint script to start the application
├── scripts
│   ├── healthcheck.sh       # Script to verify container health
├── Dockerfile               # Docker configuration file
└── README.md                # Project documentation
```

---

## **Prerequisites**

- Docker installed on your system.
- Basic knowledge of Python and Docker commands.

---

## **Steps to Build and Run**

### **1. Clone or Prepare the Project Files**
Ensure the following files are available:

- `calculator.py`: Python script for the calculator logic.
- `entrypoint.sh`: Shell script to start the Python application.
- `healthcheck.sh`: Shell script to perform container health checks.
- `Dockerfile`: Configuration file to build the Docker image.

### **2. Dockerfile Overview**

The Dockerfile uses a **multi-stage build** approach to optimize the image size:

1. **Builder Stage:**
   - Installs Python and dependencies on `ubuntu:22.04`.
   - Sets up the `/var/log` directory for logging.

2. **Runtime Stage:**
   - Copies the Python binary and necessary libraries from the builder stage.
   - Adds the application files and sets up logging.
   - Creates a non-root user (`calculator-user`) for better security.
   - Includes a health check to monitor container health.

### **3. Build the Docker Image**

Run the following command to build the Docker image:

```bash
docker build -t calculator-app .
```

### **4. Run the Docker Container**

Run the container interactively:

```bash
docker run --rm -it calculator-app
```

### **5. Persist Logs to Host Machine**

To store logs on the host machine for inspection, map the `/var/log` directory in the container to a local directory:

```bash
docker run --rm -it -v "$(pwd)/logs:/var/log" calculator-app
```

Logs will be saved to `logs/calculator.log` on the host machine.

### **6. Verify Logs**

Check the log file to ensure logs are written correctly:

```bash
cat logs/calculator.log
```

Example log entries:
```
2025-01-28 12:00:00,123 - INFO - Calculator started.
2025-01-28 12:02:10,456 - INFO - User entered a valid number: 10
2025-01-28 12:03:12,789 - INFO - Calculated: 10 + 20 = 30
2025-01-28 12:05:00,000 - INFO - Calculator exited by user.
```

### **7. Health Check**

The container includes a health check that verifies if the application is running and logging correctly. To check the health status:

1. Get the container ID:
   ```bash
   docker ps
   ```

2. Inspect the health status:
   ```bash
   docker inspect --format='{{json .State.Health}}' <container_id>
   ```

---

## **Tips for Optimization**

1. Use a smaller base image like `python:3.9-slim` to reduce image size.
2. Add more detailed logging by adjusting the logging level in `calculator.py` (e.g., `DEBUG`).
3. Ensure proper permissions for `/var/log` to avoid permission errors.

---

## **Troubleshooting**

### **Common Errors**

1. **Log File Not Found:**
   - Verify that the `/var/log` directory exists and has write permissions for `calculator-user`.

2. **Missing Libraries:**
   - Ensure all necessary Python libraries and shared libraries are copied to the runtime stage.

3. **Health Check Failing:**
   - Verify the `healthcheck.sh` script logic and container logs using:
     ```bash
     docker logs <container_id>
     ```

---

## **Conclusion**

This project demonstrates how to containerize a simple Python calculator application with logging and health checks. Using Docker makes the application portable, secure, and easy to deploy across different environments.

Feel free to extend this project with additional features or optimizations!
