# Имя файла конфигурации для Docker Compose
COMPOSE_FILE = docker-compose.yml

# Команда для запуска контейнеров в фоновом режиме
up:
	docker compose -f $(COMPOSE_FILE) up -d

# Команда для остановки контейнеров
down:
	docker compose -f $(COMPOSE_FILE) down

# Команда для перезапуска контейнеров
restart: down up

# Команда для просмотра статуса контейнеров
status:
	docker compose -f $(COMPOSE_FILE) ps
