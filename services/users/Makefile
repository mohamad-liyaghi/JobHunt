.PHONY: help build run stop test ruff

help:
	@echo "Available targets:"
	@echo "  help    - Show this help message."
	@echo "  build   - Build the docker image."
	@echo "  run     - Run the docker container."
	@echo "  stop    - Stop the docker container."
	@echo "  test    - Run the tests."
	@echo " ruff    - Run ruff check for backend code."


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
	docker exec jobhunt-users-backend pytest


ruff:
	docker exec -it jobhunt-users-backend ruff check .