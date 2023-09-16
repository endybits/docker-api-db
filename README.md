# docker-api-db

Connecting my FastAPI APP container to a MySQL container.

1. Un the directory where your dockerfile is, run `docker build -t api_image:0.0.1 .` and `docker run -d --name name_container -p 8000:80 fastapi-k8s:0.0.1` commands to create a Docker Image and a container, also verify if all work correctly.

2. Run the command `docker run -d --name db --mount src=mysqldata,dst=/var/lib/mysql -e MYSQL_ROOT_PASSWORD=YOUR_CUSTOM_PASSWQRD mysql:latest` to create a mysql container.

3. Navigate into using ` docker exec -ti db bash` then go into mysql and create a new db.

4. Remove your container and repeat the steps 2 and 3. Then verify that your created db persist on your new container.

5. Now let's create a network.
