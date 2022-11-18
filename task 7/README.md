# docker_files task 7
### Сборка образа 
```
docker build -t task7:1.0 . 
```
### Список образов docker
```
docker images
```
### Загрузка в репозиторий
```
docker login
docker tag task7:1.0 simanenkojulia/itmo:task7-1.0 
docker push simanenkojulia/itmo:task7-1.0 
```
### Запуск контейнера из репозитория
```
docker pull docker push <login>/<repository_name>:<container_name>
docker run -p <docker_port>:<container_port> <login>/<repository_name>:<container_name>
docker stop <id>

docker-compose -f docker-compose.yaml pull
docker-compose -f docker-compose.yaml up -d
```


