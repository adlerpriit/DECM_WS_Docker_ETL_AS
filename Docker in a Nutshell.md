## Docker in a Nutshell
### What is Docker?
Docker is a tool that helps you package your applications and their dependencies into containers. Containers are lightweight, portable, and isolate your app from the host machine, ensuring a consistent environment wherever you run them (your computer, a server, or the cloud).

### Why Use Containers?
* Consistency: “It works on my machine” is no longer an issue.
* Isolation: Each container runs in its own environment without interfering with others.
* Portability: You can run containers anywhere Docker is supported.
* Efficiency: Containers share the host OS kernel, making them more resource-efficient than full virtual machines.
### Main Docker Concepts
1. Images
   * A Docker image is a blueprint for running a container.
   * It includes everything needed to run an application: code, libraries, tools, dependencies, etc.
2. Containers
   * A container is a running instance of an image.
   * You can start, stop, pause, and remove containers.
3. Dockerfile
   * A text file with instructions for building a Docker image.
   * Specifies the base image, dependencies, and any commands needed to set up the environment or run your app.
4. Docker Hub (Registry)
   * A public repository of Docker images.
   * You can pull images from Docker Hub, or push your own images there (or a private registry).
### Typical Docker Workflow
1. Write a Dockerfile
   * Start from a base image (e.g., FROM ubuntu:latest, FROM node:alpine, etc.).
   * Install and configure dependencies.
   * Copy in your source code.
   * Define a command to run when the container starts.
2. Build the Image
```bash
docker build -t your-image-name .
```
   * The -t tag names your image.
   * The . indicates the Dockerfile is in the current directory.
3. Run a Container
```bash
docker run -d -p 3000:3000 --name mycontainer your-image-name
```
   * -d runs the container in the background (detached mode).
   * -p 3000:3000 publishes the container’s internal port 3000 to your computer’s port 3000.
   * --name mycontainer gives the container a friendly name (optional).
4. Check Running Containers

```bash
docker ps
```
   * Lists all currently running containers.
5. Stop & Remove Containers

```bash
docker stop mycontainer
docker rm mycontainer
```
   * Always stop the container before removing it.
### Common Commands (Cheat Sheet)
```bash
# Pull an image from a registry
docker pull <image-name>

# List all local images
docker images

# Build an image from a Dockerfile
docker build -t <image-name> <path>

# Run a container from an image
docker run [options] <image-name>

# Show running containers
docker ps

# Show all containers (including stopped ones)
docker ps -a

# Stop a running container
docker stop <container-name-or-id>

# Remove a stopped container
docker rm <container-name-or-id>

# Remove an image
docker rmi <image-name-or-id>

# Display logs for a container
docker logs <container-name-or-id>

# Run a command inside a running container
docker exec -it <container-name-or-id> <command>
```
### Volumes and Data Persistence
* Volumes let you store and persist data outside the container’s own filesystem.
* Example: mounting a local folder inside a container to store user data or database files that survive container restarts.
```bash
docker run -d -v /local/path:/container/path <image-name>
```
### Docker Compose
When you have multiple containers (e.g., a web app, a database, etc.) that need to work together:

* Docker Compose uses a docker-compose.yml file to define and run multi-container applications.
* Start all services with one command:
```bash
docker-compose up -d

```
### Dev Containers and VS Code
A dev container is essentially a Docker container configured for development. VS Code’s “Dev Containers” feature allows you to:
* Open a project inside a container that has all the necessary tools and libraries.
* Avoid installing those tools on your local machine.
* Share the exact same setup across different computers or teammates.
### Quick Steps to Use Dev Containers in VS Code
1. Install the Dev Containers (or Remote – Containers) extension.
2. Provide a .devcontainer/devcontainer.json file specifying the base image and settings.
3. Open Folder in Container via the extension.
4. VS Code will build and start the container, installing dependencies so you can code immediately inside a consistent environment.

### Further Resources
* Official Docker Documentation: https://docs.docker.com
* Docker Hub: https://hub.docker.com
* Dockerfile Reference: https://docs.docker.com/engine/reference/builder/
* Docker Compose Reference: https://docs.docker.com/compose/
