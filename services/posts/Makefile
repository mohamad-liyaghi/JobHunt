.PHONY: help build run stop confmap

help:
	@echo "Available targets:"
	@echo "  help          - Show this help message."
	@echo "  build         - Build the docker image."
	@echo "  run           - Run the docker container."
	@echo "  stop          - Stop the docker container."
	@echo "  confmap - Create a configmap for the posts service."

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

confmap:
	kubectl create configmap jobhunt-posts-env --from-env-file=.env
