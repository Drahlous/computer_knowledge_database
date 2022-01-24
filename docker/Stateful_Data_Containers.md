# Stateful Docker Containers

There are two ways to approach stateful containers:

1. Mount a volume with `-v <host-dir>:<container-dir>`
2. Create **Data Containers**

## Data Containers

A **Data Container** is only used to store and manage data.
We'll use busybox as a lightweight base, and supply the `-v` option to define where other containers will read and store data.

```bash
docker create -v /config --name dataContainer busybox
```

Next we can copy our files into the container with `cp`. We'll copy some file "config.conf" into our data container's `/config` directory.

```bash
docker cp config.conf dataContainer:/config/
```

When we're starting other containers, we can reference this dataContainer with the `--volumes-from` flag.

```bash
docker run --volumes-from dataContainer ubuntu ls /config
```

[up](README.md#table-of-contents)
