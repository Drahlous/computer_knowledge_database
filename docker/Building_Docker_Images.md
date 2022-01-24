# Docker Images

Docker images start from a **Base Image**.
The base image should include all **dependencies** required by your application.

The base image is defined as an instruction in the **Dockerfile**.
The Dockerfile contains instructions on how to **build the docker image**.

```Docker
# Define the base image
FROM nginx:alpine

# Copy the content of the current directory to a specified location within the container
COPY . /usr/share/nginx/html
```

Now you can build and run the dockerfile.

```bash
#Adding the `-t` flag allows us to specify a user-friendly image name.
docker build -t webserver-image:v1 .
docker run -d -p 80:80 webserver-image:v1
```

* * *

## Building Images

We use a **Base Image** as the foundation of other images.

```Dockerfile
# `FROM` is used to specify the base image:
FROM <image-name>:<tag>
FROM nginx:1.11-alpine

# `RUN` allows you to execute any command like you would from the terminal. 
# Results are persistent within the image!

# `COPY <src> <dst>` allows you to copy file into the container's image
COPY index.html /usr/share/nginx/html/index.html

# `EXPOSE <port>` indicates which ports should be open and bound.
EXPOSE 80

# `CMD` Defines the default command to be run when the container is launched
CMD ["nginx", "-a", "arga val", "-b", "argb val"]

# `ENTRYPOINT` is an alternative to CMD.
# CMD is completely overwritten if arguments are provided.
# With ENTRYPOINT, arguments are instead appended to the command.

```

* * *

## OnBuild Optimization

We can include the **ONBUILD** keyword to indicate that a command should be run later, when the image is used as a **Base Build** for some other image.

```Dockerfile
FROM node:7
RUN mkdir -p /usr/src/app

ONBUILD COPY package.json /usr/src/app
ONBUILD RUN npm install
ONBUILD COPY . /usr/src/app

CMD ["npm", "start"]
```

This way, the Dockerfile for our real application can be much simpler, we just have to set the port!

```Dockerfile
From node:7-onbuild
EXPOSE 3000
```

* * *

## Ignoring files during build

Say for example you have a sensitive file "passwords.txt", but we need it during the build.
One option is to `COPY -> use -> DELETE`.

You can also ignore files with a **.dockerignore** file, it works just like a **.gitignore**.
You'll want to ignore ".git" directories, along with dependencies that are downloaded/built like node modules.

* * *

## Optimizing Images with Multi-Stage Builds

We'll use **multi-stage builds** to make our images smaller, and faster to build.

Previously, this problem would have been solved with two dockerfiles:

- The first would have the steps to build the binary and artifacts using a development container.
- The second would be optimized for production, it would not include development tools

## Multi Stage Dockerfile

```Dockerfile
# First Stage
# Use the Golang SDK to build a binary
FROM golang:1.6-alpine

RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Second Stage
# Copy the resulting binary into an optimized Docker Image
FROM alpine
EXPOSE 80
CMD ["/app"]

COPY --from=0 /app/main /app
```

We'll build the image with the same syntax as before:

```bash
docker build -f Dockerfile.multi -t golang-app .
```

This will result in two images.

- An **untagged** image that was used during the first stage
- Our smaller **target** image

We can test the image with no other changes required.

```bash
docker run -d -p 80:80 golang-app
curl localhost
```
