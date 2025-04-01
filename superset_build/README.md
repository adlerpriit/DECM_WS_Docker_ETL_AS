## Instructions 

on how to use the Superset build folder and how to build custom images based on existing superset image. Adding new database support.

```bash
# Build the image (Uses the Dockerfile in this directory)
docker build -t superset-build .

# Secret key should be changed and kept secret, not published to GitHub :)
docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset superset-build

# Explanation for the -v ${PWD}:/data:rw flag:
# This flag mounts the current working directory (${PWD}) on the host machine to the /data directory inside the container.
# You should replace ${PWD} with the absolute path to the folder where their data files will be stored.
# For example: -v /Users/yourname/superset_data:/data:rw
# Or if you are in the folder where the data files are located, you can use -v $(pwd):/data:rw
# The :rw option allows read and write access to the mounted directory.
# This ensures that the container has access to the necessary data files.

# Update user, firstname, lastname, email and password as you see fit
docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init
```

### Rebuilding the Image

If you need to rebuild the image (e.g., after making changes to the Dockerfile or other configuration files), you can use the following commands:

```bash
# Remove the existing container (if running)
docker stop superset
docker rm superset

# Rebuild the image
docker build -t superset-build .

# Run the container again with the updated image
docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset superset-build
```

### Removing Dangling Images

Dangling images are unused Docker images that can take up unnecessary space. To remove them, use the following command:

```bash
docker image prune -f
```

### Important Notes

- **Host Machine Execution**: All the commands in this README should be executed on the host machine where Docker is installed. While the project includes a `devcontainer`, these commands are not intended to be run inside the development container.
- **Data Directory**: Ensure that the directory you mount with the `-v` flag contains the data files you want to use with Superset. This directory will be accessible inside the container at `/data`.

Additional up-to-date documentation about Superset can be found at [https://superset.apache.org/docs/intro](https://superset.apache.org/docs/intro).