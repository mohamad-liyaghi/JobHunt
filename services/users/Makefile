.PHONY: help build run stop test ruff confmap

help:
	@echo "Available targets:"
	@echo "  help          - Show this help message."
	@echo "  build         - Build the docker image."
	@echo "  run           - Run the docker container."
	@echo "  stop          - Stop the docker container."
	@echo "  test          - Run the tests."
	@echo "  ruff          - Run ruff check for backend code."
	@echo "  confmap - Create a configmap for the user service."

build:
	docker compose build

run:
ifeq ($(DETACHED),true)
	docker compose up -d
else
	docker compose up
endif

stop:
	docker compose down

test:
	docker exec jobhunt-users-backend python -m pytest tests/

ruff:
	docker exec -it jobhunt-users-backend ruff check .

confmap:
	kubectl create configmap jobhunt-user-env --from-env-file=./env/pg.env --from-env-file=./env/jwt.env
