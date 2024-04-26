.PHONY: help k8s deploy

help:
	@echo "Available targets:"
	@echo "  help          - Show this help message."
	@echo "  k8s            - Create Kubernetes Resources."
	@echo "  deploy          - Deploy The Project On Kubernetes Cluster."


make k8s:
	kubectl apply -f k8s/ --recursive


deploy:
	cd services/users/ && make confmap
	cd services/posts/ && make confmap
	cd ..
	make k8s