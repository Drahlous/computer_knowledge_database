# Load Balancing Containers

We'll explore how to use the NGINX web server to load balance requests between two containers.

Docker provides serveral ways for containers to communicate. We explored links, which configure the container using environment variables and host entry's.

The **Service Discovery Pattern** is where the application uses a third-party system to identify the location of a target service. For example, if our application wanted to talk to a database, it would ask an API what the address of the database is.

This pattern allows you to **quickly reconfigure** and **scale** your architecture with better **fault tolerance** than fixed locations.

## NGINX Proxy

In this example, we want an NGINX service which can dynamically discover and update its load balancing configuration when new containers are added.
This implementation already exists, it's called **nginx-proxy**.

**Nginx-proxy** accepts HTTP requests, then proxies the request to the appropriate container (based on the request Hostname).

There are three key properties that must be configured when launching a proxy container:

- The container must be bound to **port 80** on the host.
  - This ensures that all HTTP requests are handled by the proxy.
- The **docker.sock** file must be mounted.
  - It's a connection to the docker daemon running on the host
  - Nginx-proxy uses this to listen for events
- We can set an optional `-e DEFAULTHOST=<domain>`
  - If a request arrives without a specified host, it will be redirected here.

```bash
docker run -d -p 80:80 -e DEFAULT_HOST=proxy.example -v /var/run/docker.sock:/tmp/docker.sock:ro --name nginx jwilder/nginx-proxy

# Because we've added DEFAULT_HOST,
# any requests that arrive will be directed to the container
# that has been assigned with the host "proxy.example"

# We'll make a request, but we expect a 503 error since we have no containers
curl http://docker
```

## Single Host

Now **Nginx-proxy** is listening to events from Docker.

For Nginx-proxy to start sending requests to a container, we need to set the environment variable **VIRTUAL_HOST**. This defines where requests will come from. In this case, we'll match the virtual host to the default host, **proxy.example**

```bash
docker run -d -p 80 -e VIRTUAL_HOST=proxy.example katacoda/docker-http-server

# Now our request should be processed
curl http://docker
```

## Cluster

If we were to launch a secon container with the same VIRTUAL_HOST, then nginx-proxy will configure the system in a **round-robin load balancing** scenario:

- The **first request** is sent to the **first container**
- The **second request** is sent to the **second container**

```bash
# Launch a second container using the same command as before
docker run -d -p 80 -e VIRTUAL_HOST=proxy.example katacoda/docker-http-server

# If we repeatedly send requests, we'll see them being alternativly handled by the two containers
curl http://docker
```

## Generated NGINX Configuration

While nginx-proxy will automatically create and configure NGINX for us, we can see the final configuration that it made:

```bash
docker exec nginx cat /etc/nginx/conf.d/default.conf
```

* * *

## Docker Swarm

We'll learn how to initialize a cluster in **Docker Swarm Mode** and deploy networked containers using the built-in **Docker Orchestration**.

**Swarm Mode** enables the ability to deploy containers across **multiple Docker hosts**.
It uses overlay networks for service discovery and a built-in load balancer for scaling the services.

## Key Concepts

- **Node**: A Node is an instance of the Docker Engine connected to the swarm. Nodes are either **managers** or **workers**.
  - **Managers** schedule which containers to run and where
  - **Workers** execute the tasks
- **Services**: A Service is a high-level concept relating to a collection of tasks to be executed by workers.
  - An example of a service is an HTTP server running as a Docker Container on three nodes.
- **Load Balancing**: Docker includes a built-in load balancer to process requests across all containers.

* * *

## Initialize Swarm Mode

By default, Docker works as an isolated single-node.
**Swarm Mode** turns it into a **multi-host** **cluster-aware** engine.

The first node to initialize the Swarm Mode becomes the **Manager**.
As new nodes join, they can adjust their roles between managers or workers.
*You should run 3 to 5 managers in production to ensure high availablility*

```bash

# You can find an overview of the commands with --help
$docker swarm --help

# Create a Swarm Mode Cluster
$docker swarm init
Swarm initialized: current node (dy72cua9m3ruay1ebxelb1un2) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-53u343zuq4nvb66b2qj62deyddj4q03ozj5npqu8fp36ag8tji-adckignv2e49vcx4vkjr8jjjr 172.17.0.41:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

## Join the Cluster

If some nodes crash, the containers which were running on those hosts will be automatically rescheduled onto other available nodes, ensuring high-availability.

Docker uses an additional port **2377** for managing the Swarm. This port should be blocked from public access, and only accessed by trusted users and nodes.

Let's get the token that's required to add a worker to the cluster.
In this demo, we'll get it with `swarm join-token`, but in production, *this token should be stored securely and only given to trusted individuals*.

```bash
# Ask the manager what the token is
token=$(ssh -o StrictHostKeyChecking=no 172.17.0.41 "docker swarm join-token -q worker") && echo $token

# On the second host, join the cluster
docker swarm join 172.17.0.41:2377 --token $token

# Now we can view all nodes in the cluster
docker node ls
```

## Create an Overlay Network

In previous versions, Docker required an external key-value store (like Consul) to ensure consistency across the network.
Now this functionality is incorporated internally into docker.

The syntax is the same as before, but we add the `overlay` keyword when creating the network.

```bash
docker network create -d overlay skynet
```

## Deploy a Service

By default, docker uses a **Spread Replication Model** to decide which containers should run on which hosts.
The spread approach ensures that containers are deployed **evenly across the cluster**.
If a node is removed from the cluster, the workload is **rescheduled across the remaining nodes**.

In this example, we're deploying the image *katacoda/docker-http-server* with the name *http*.
It will be attached to the *skynet* network that we just created.
`docker service create --name http --network skynet`

For replication and availability, we'll run two instances of replicas of the container across the cluster.
`--replicas 2`

Finally, we load balance the containers together on port 80.
If we send an HTTP request to any of the nodes, the cluster will decide which node to respond on.
*The node which accepted the request may be different from the node where the container responds.*

In full:

```bash
# Create the "http" service on the "skynet" network
docker service create --name http --network skynet --replicas 2 -p 80:80 katacoda/docker-http-server

# View the currently-running services
docker service ls

# If we make repeated HTTP requests, we'll see alternate hosts handling the requests
curl host01
```

## Inspect State

We can use the Service concept to inspect the health and state of the cluster.

```bash
# View the list of all tasks associated with the "http" service
docker service ps http

# View the details of a particular service
docker service inspect --pretty http

# On each node, we can we what task we're currently running
# "self" refers to the manager node Leader
docker node ps self

# We can use the ID of a node to query individual hosts
docker node ps $(docker node ls -q | head -n1)
```

## Scale the Service

A **Service** allows us to scale the number of instances of a task that are running across the cluster.

```bash
# Run the http service across 5 containers
docker service scale http=5

# We can see the new nodes on each host
docker ps
```
