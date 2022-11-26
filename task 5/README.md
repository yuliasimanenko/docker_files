# docker_files 
### Сборка образа 
```
docker build --tag docker_files .
```
### Список образов docker
```
docker images
```
### Загрузка в репозиторий
```
docker login
docker tag docker_files simanenkojulia/itmo:docker_files
docker push simanenkojulia/itmo:docker_files
```
### Запуск контейнера из репозитория
```
docker pull docker push <login>/<repository_name>:<container_name>
docker run -p <docker_port>:<container_port> <login>/<repository_name>:<container_name>
docker stop <id>
```


