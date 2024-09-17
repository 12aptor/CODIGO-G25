# Docker

## Comandos

### Build

```bash
# docker build -t {image_name} .
docker build -t express-docker .
```

### Run (Docker)

```bash
# docker run -p {host_port}:{container_por} -d {image_name}
# -d => Daemon: ejecutar en segundo plano
docker run -p 5000:3000 express-docker
```

### Show Executing Containers

```bash
docker ps
```

### Stop Executing Containers

```bash
docker stop {container_id}
```

### Show All Containers

```bash
docker ps -a
```

### Remove Containers

```bash
docker rm {container_id}
```

### Remove All Containers (Warning)

```bash
docker rm -f $(docker ps -a -q)
```
### Show Images

```bash
docker images
```

### Remove Images

```bash
docker rmi {image_name}
```

### Remove All Images (Warning)

```bash
docker rmi -f $(docker images -q)
```

### Show Container Logs

```bash
docker logs {container_id}
```