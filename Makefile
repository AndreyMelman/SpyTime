DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker-compose.yml
APP_CONTAINER = app

.PHONY: app app-down app-shell app-logs test

app:
	${DC} -f ${APP_FILE} up --build -d

app-down:
	${DC} -f ${APP_FILE} down

app-shell:
	${EXEC} ${APP_CONTAINER} bash

app-logs:
	${LOGS} ${APP_CONTAINER} -f