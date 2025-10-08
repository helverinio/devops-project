# Makefile for Blacklist Microservice

.PHONY: help install run test clean docker-build docker-run docker-stop init-db

help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  run         - Run the application"
	@echo "  test        - Run tests"
	@echo "  clean       - Clean Python cache files"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run  - Run with Docker Compose"
	@echo "  docker-stop - Stop Docker Compose"
	@echo "  init-db     - Initialize database"
	@echo "  generate-token - Generate JWT token for testing"

install:
	pip install -r requirements.txt

run:
	python run.py

test:
	python -m pytest tests/ -v

test-simple:
	python tests/test_api.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

docker-build:
	docker build -t blacklist-api .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f blacklist-api

init-db:
	python scripts/init_db.py init

drop-db:
	python scripts/init_db.py drop

generate-token:
	python scripts/generate_token.py

# Development helpers
dev-setup: install init-db
	@echo "Development environment ready!"

dev-run: clean run

# Production helpers
prod-build: clean docker-build

prod-deploy: docker-run
