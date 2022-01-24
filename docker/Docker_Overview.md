# Docker

- Containers are a *paradigm* for application development and deployment.

- Containers use Linux Kernel features to run applications in an isolated way on a shared machine
  - namespaces
  - cgroups
  - capabilities
- Application source code, Docker build info, and automation code should be stored together on github.

* * *

## Commands

```bash
# Find existing images on the Docker registry
docker search <image>

# List all running containers
docker ps

# Get more details about a container
# docker inspect <name|id>

# Display messages the container has written to stderr or stdout
docker logs <name|id>
```

* * *

## Formatting Output from docker ps

The standard `docker ps` command outputs the name, image used, command, uptime, and port info.
It's output in a tabular format:
CONTAINER ID | IMAGE | COMMAND | CREATED | STATUS | PORTS | NAMES
---|---|---|---|---|---|---
a05ef43766d1 | redis | "docker-entrypoint.s…" | 4 minutes ago | Up 4 minutes | 6379/tcp | pedantic_ride

We can limit which columns are displayed using the `--format` parameter.
The pretty-printing is configured using a ([Go Template](../../undefined)) syntax:

```bash

$docker ps --format '{{.Names}} container is using {{.Image}} image'
pedantic_ride container is using redis image

# And since it's using Go templates, it includes helper functions like "table"
$docker ps --format 'table {{.Names}}\t{{.Image}}'
NAMES               IMAGE
pedantic_ride       redis
```

## Adding Docker Inspect

The **docker ps** command doesn't give us all the information about a container.
We'll also want to be able to display info from **docker inspect**.

The output from **inspect** is in a JSON format, but we can use the same syntax

```bash
# Note the multi-level JSON parsing with .NetworkSettings.IPAddress
docker ps -q | xargs docker inspect --format '{{ .Id }} - {{.Name}} - {{ .NetworkSettings.IPAddress }}'
```

* * *

## Ports

Containers are in a sandbox

- if a service must be accessible by a process outside the container, we'll need to expose the **port** via the **host**
- ports are bound when the container starts using `-p <host-port>:<container-port>`

```bash
docker run -d --name redisHostPort -p 6379:6379 redis:latest
```

By default, the port on host is mapped to `0.0.0.0` which means **all ip-addresses**. You can specify a specific ip with `-p 127.0.0.1:6379:6379`

If you run a process on a **fixed-port** then you can only run one instance! You can randomly assign one and discover it instead with `port <name>`:

```bash
docker run -d --name redisDynamic -p 6379 redis:latest
docker port redisDynamic 6379
```

* * *

## Persistent Data

Containers are designed to be **stateless**.
You can bind directories (volumes): `-v <host-dir>:<container:dir>`.
This way, the data is stored on the host, and is persistent.

For example, say we know that Redis stores logs and data to the `/data` directory.
We should map this to the host as `/opt/docker/data/redis`:

```bash
docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis
```

* * *

## Foreground & Background Containers

Previously, we've run docker with the `-d` flag, meaning "run this in the background as a `detatched` container".

We can use `-it` instead to get an `interactive terminal`.

```bash
docker run -it ubuntu bash
```

* * *

## Environment Variables

Docker images should be built to be transferable between environments without issues or rebuilding.

Environment variables can be defined when you launch a container.

```bash
docker run -d --name my_production_running_app -e NODE_ENV=production -p 3000:3000 my-nodejs-app
```

* * *

## Docker Stats

When you're running production containers, it's important to monitor the runtime metrics like CPU and memory usage.
Docker has some built in tools for this purpose

## Single Container

Say we have an existing running container with the name *nginx*. We can check its stats with the **stats** command:

```bash
# This will provide live data from the container
docker stats nginx
```

## Multiple Containers

If we want to view the stats for multiple containers, we can use xargs.
We'll get the list of running containers with `docker ps`, then pipe them as arguments to `docker stats`.

```bash
docker ps -q | xargs docker stats
```
