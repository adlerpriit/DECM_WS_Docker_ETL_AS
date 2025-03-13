## Instructions on how to use the Superset build folder and how to build custom images based on existing superset image. Adding new database support.

```bash
# Build the image
docker build -t superset-build .
# Secret key should be changed and kept secret, not published to GitHub :)
docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset superset-build
# Update user, firstname, lastname, email and password as you see fit
docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init
```

Additional up to date documentation about superset can be found at https://superset.apache.org/docs/intro