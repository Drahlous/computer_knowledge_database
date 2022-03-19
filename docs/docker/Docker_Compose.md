# Docker Compose

[Docker Compose Docs](https://docs.docker.com/compose/compose-file/)
Docker compose is configured using the YAML file **docker-compose.yml**.
It defines all of the containers and settings needed to launch the set of clusters.

The properties map to the way you use the **docker run** commands, but they're now stored in source control alongside the code.

The formate is based on YAML:

```yaml
container_name:
 property: value
  - or options
```

## Defining a container

We want a Node.js application which connects to Redis. We'll start by defining the **docker-compose.yml** to launch the Node.js application.

We'll name the container "web", and set the **build property** to the current directory.
This is similar to the commands in `docker build -t web .`

```yaml
web:
 build: .
```

If we want to link containers together, we'll specify a **links property**. This example would link the redis source container (defined in the same file) and assign the same name to the alias.

```yaml
links:
 - redis
```

The same format is used for other properties, such as the **ports property**.

```yaml
ports:
 - "3000"
 - "8000"
```

## Defining a second container

Previously, we used the Dockerfile in the current directory as the base for our container.
In this step, we'll use an **existing image from Docker Hub** as a second container.

We can simply add to the same YAML file, using the same format as before. Here, we'll specify the **image property** and the **volumes property**.

```yaml
redis:
 image: redis:alpine
 volumes:
  - /var/redis/data:/data
```

## Docker Up

At this stage, our compose file has the following contents:

```yaml
web:
 build: .
 ports:
  - "3001"
 links:
  - redis

redis:
 image: redis:alpine
 volumes:
  - /var/redis/data:/data
```

Now that we have a **docker-compose.yml** file, we can launch *all* of the defined applications with the **up** command:

```bash
# The "-d" flag has the same result as it does in "docker run"
# It causes the containers to be run in the background
docker-compose up -d
```

If you want to run a single container, you could use `docker-compose up <name>`

* * *

## Docker Management

Docker Compose can also be used to manage all containers easily.

```bash
# Check the details of the launched containers
docker-compose ps

# Access all of the logs via a single stream
docker-compose logs

# Checkout the other available commands by running
docker-compose
```

## Docker Scale

Docker Compose understands how to launch the application containers, so it can also be used to **scale the number of running containers**.

The **scale** option allows you to specify the service you want, then the **number of instances** of that service.

```bash
# Scale the number of containers we want running our "web" service
docker-compose scale web=3

# You can also scale back down
docker compose scale web=1
```

## Stopping Containers

We can stop and remove containers with the same intuition we used in starting them:

```bash
# Stop a set of containers
docker-compose stop

# Remove all containers
docker-compose rm
```

[up](README.md#table-of-contents)
