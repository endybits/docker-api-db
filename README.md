# docker-api-db 🐳📦

Connecting my FastAPI APP container to a MySQL container.

1. In the directory where your Dockerfile is located, run `docker build -t api_image:0.0.1 .` command.

2. Create a MySQL container by running the command:

   ```bash
   docker run -d --name db --mount src=mysqldata,dst=/var/lib/mysql -e MYSQL_ROOT_PASSWORD=YOUR_CUSTOM_PASSWORD mysql:latest
   ```
   
3. Run a container based on your api_image:

   ```bash
   docker run -d --name api-container -p 8080:80 --env HOST_DB=db --env PASSWORD_DB=your_mysql_root_password api_image:0.0.1
   ``` 
  
  
  - Ensure that HOST_DB is the name of your MySQL container, and PASSWORD_DB is the MYSQL_ROOT_PASSWORD provided to the MySQL container.

    ![image](https://github.com/endybits/docker-api-db/assets/22806426/6669ef1a-b97e-4ed5-b4a9-acc3c7683ffc) 
As you can see, the response is 200 Ok, but we got our customized connection error: `"db connection": "Boom 💣💥! DB connection failed"`. This is because we need to communicate the containers with each other.

4. Now, let's create a network.

   a - Create a docker network with the command
   ```bash 
   docker network create --attachable api-net
   ```
   `api-net` is my chosen name; so, you can use any other, The flag `--attachable` allows our network to link containers.

   b - Link the API and DB containers to the network with these commands:
   ```bash
   docker network connect app-db api-container
   docker network disconnect app-db db
   ```

   c - Check the endpoint
   ![image](https://github.com/endybits/docker-api-db/assets/22806426/c2b27ac0-c0f0-4814-b2ad-4627148c0185)
   Now, you'll get a `"db connection": "DB connection successful 💫"` response. Your FastAPI app container is successfully connected to the MySQL container!
