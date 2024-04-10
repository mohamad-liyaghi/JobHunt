.PHONY: help deploy

help:
	@echo "Available targets:"
	@echo "  help          - Show this help message."
	@echo "  deploy          - Deploy The Project On Kubernetes Cluster."



deploy:
	cd services/users/ && make confmap
	cd services/posts/ && make confmap
	cd ..
	kubectl apply -f k8s/users
	kubectl apply -f k8s/posts