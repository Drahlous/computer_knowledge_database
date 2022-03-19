# Docker

This is my set of personal notes on the Docker paradigm, collected while completing the [Katacode Docker Courses](https://www.katacoda.com/courses/docker). Although I've restructured and restated the information to my preferences, some information is directly duplicated. Please check out the Katacode courses, they're an excellent entrypoint into the ecosystem.

## Table of Contents

1. [Docker Overview](./Docker_Overview.md)
2. [Building Images](./Building_Docker_Images.md)
3. [Stateful Data Containers](./Stateful_Data_Containers.md)
4. [Container Networking](./Container_Networking.md)
5. [Docker Compose](./Docker_Compose.md)
6. [Docker Clusters](./Docker_Clusters.md)

## Quick Reference

```bash
# Build the image defined in the current directory
docker build -t <name> .

# Run a container
docker run <name>
docker run -d <name>  # as a "detatched" background process
docker run -it <name> # as an "interactive terminal" foreground process
docker run -e NODE_ENV=production # set the NODE_ENV environment variable

# Start services defined in docker-compose.yml
docker-compose up

# List all running containers
docker ps
docker ps -q    # quiet, only show the container id's

# Get more details about a container
docker inspect <name|id>

# Display messages the container has written to stderr or stdout
docker logs <name|id>

# Find existing images on the Docker registry
docker search <image>

```
