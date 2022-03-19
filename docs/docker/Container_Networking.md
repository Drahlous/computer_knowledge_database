# Communicating Between Containers

In this example, we'll use **Redis**, which is a fast, open-source, key-value data store.

```bash
docker run -d --name redis-server redis
```

## Create a link

When we're launching a new container, we can connect to a source container with the `--link <container-name|id>:<alias>`.

Here, we'll link an Alpine server to our redis-server host.

First, Docker will set some environment variables based on the linked container. These give you a way to reference information like Ports, IP addresses via known names.

You can output the environment variables with the `env` command:

```bash
docker run --link redis-server:redis alpine env
```

Second, Docker will update the **HOSTS** file of the container. It will add an entry for our source container consisting of three names: the original, the alias, and the hash-id. You can see the entry in the hosts file at `/etc/hosts`:

```bash
docker run --link redis-server:redis alpine cat /etc/hosts
```

This is the full command: We'll run an alpine container, link it to our redis server, and ping redis to make sure it's connected.

```bash
docker run --link redis-server:redis alpine ping -c 1 redis
```

## Connect to an App

Using this link method, we can connect applications in the usual way, as if they were not running in containers.

```bash
docker run -d -p 3000:3000 --link redis-server:redis katacoda/redis-node-docker-example
```

We'll test the connection with `curl`

```bash
curl docker:3000
```

* * *

## Networks between Containers

Instead of using **links**, we'll use **networks** to allow containers to come and go more freely.
Docker has an Embedded DNS Server.

## Create a network

```bash
# Create a network
docker network create backend-network

# Connect to a network
docker run -d --name=redis --net=backend-network redis

# Get some info about the network
docker run --net=backend-network alpine env
docker run --net=backend-network alpine cat /etc/hosts

# Check that the DNS server is assigned to the container in resolv.conf
# It should be 127.0.0.11 in this case
docker run --net=backend-network alpine cat /etc/resolv.conf

# Check that the DNS server returns the IP address of the correct Container
docker run --net=backend-network alpine ping -c1 redis

```

## Connect two containers

```bash
# Create a network
docker network create frontend-network

# Attach existing containers to the network
docker network connect frontend-network redis

# Launch the webserver, connect it to our network
docker run -d -p 3000:3000 --net=frontend-network katacoda/redis-node-docker-example

# Test with curl
curl docker:3000
```

## Create Aliases

Links still work when using networks. They provide an **alias** for a container name. This gives the container an extra DNS entry name and way to be discovered.

```bash
# We'll create another network
docker network create frontend-network2

# Connect our Redis instance to the network with the alias "db"
docker network connect --alias db frontend-network2 redis

# We'll run an instance of alpine to ping the db
docker run --net=frontend-network2 alpine ping -c1 db
```

## Disconnect Containers

```bash
# List all the networks on our host
docker network ls

# Explore the network, see which containers are attached.
docker network inspect frontend-network

# Disconnect our redis container from the frontend-network
docker network disconnect frontend-network redis

```

[up](README.md#table-of-contents)
