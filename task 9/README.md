# docker_files task 9
### Локальное расположение реестра
```
image: 127.0.0.1:5000/swarm-task
```
### Реплики
```
deploy:
	mode: replicated
	replicas: 4
```
## Работа со SWARM
### Инициализация
```
docker swarm init
```
### Создание реестра
```
	docker service create --name registry --publish published=5000,target=5000 registry:2 
```
### Отправка приложения в реестр
```
	docker-compose push
```
### Развертывание приложения
```
	docker stack deploy --compose-file docker-compose.yaml web-swarm-task
```
### Посмотреть информацию 
```
	docker stack services web-swarm-task
    docker service ls
```
### Удаление
```
	docker stack rm web-swarm-task
    docker service rm registry
    docker swarm leave --force
```

Если сравнивать swarm и Kubernetes, то они окажутся похожи. В Kubernetes порядок действий такой:
- инициализация
- настройка сети
- создение worker nodes
В целом Kubernetes предоставляет больше возможностей, но и является более сложным инструментом.