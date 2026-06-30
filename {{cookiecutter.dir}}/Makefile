# Makefile for {{ cookiecutter.project_name }} - {{ cookiecutter.display_name }}

.PHONY: help setup run docker-up docker-down docker-build migrate makemigrations test shell collectstatic clean lint

# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ---------------------------------------------------------------------------
# Development
# ---------------------------------------------------------------------------

setup: ## Run the full project setup (git, submodules, .env, poetry, migrate)
	@echo "Running full setup..."
	@bash -c '\
		if [ ! -d .git ]; then \
			echo "Initializing git repository..."; \
			git init; \
		fi; \
		if [ -f .gitmodules ]; then \
			echo "Initializing submodules..."; \
			git submodule init; \
			git submodule update; \
		fi; \
		if [ ! -f .env ]; then \
			echo "Creating .env from env.example..."; \
			cp env.example .env; \
		fi; \
		if ! command -v poetry >/dev/null 2>&1; then \
			echo "Installing Poetry..."; \
			curl -sSL https://install.python-poetry.org | python3 -; \
			export PATH="$$HOME/.local/bin:$$PATH"; \
		fi; \
		echo "Installing dependencies..."; \
		poetry lock --no-update; \
		poetry install --no-root; \
		echo "Running migrations..."; \
		poetry run python manage.py migrate; \
		echo "✅ Setup complete!"
	'

run: ## Run the Django development server (localhost:8000)
	poetry run python manage.py runserver

migrate: ## Apply database migrations
	poetry run python manage.py migrate

makemigrations: ## Create new database migrations
	poetry run python manage.py makemigrations

createsuperuser: ## Create a Django superuser
	poetry run python manage.py createsuperuser

collectstatic: ## Collect static files
	poetry run python manage.py collectstatic --noinput

shell: ## Open Django shell
	poetry run python manage.py shell

test: ## Run the test suite
	poetry run pytest

# ---------------------------------------------------------------------------
# Docker
# ---------------------------------------------------------------------------

docker-up: ## Start all services in Docker (build if needed)
	docker compose up --build -d

docker-down: ## Stop all Docker services
	docker compose down

docker-down-v: ## Stop Docker services and remove volumes
	docker compose down -v

docker-logs: ## Show Docker compose logs
	docker compose logs -f

docker-shell: ## Open a shell in the running web container
	docker compose exec web sh

docker-migrate: ## Run migrations inside Docker
	docker compose exec web poetry run python manage.py migrate

docker-makemigrations: ## Create migrations inside Docker
	docker compose exec web poetry run python manage.py makemigrations

docker-test: ## Run tests inside Docker
	docker compose exec web poetry run pytest

# ---------------------------------------------------------------------------
# Lint / Format
# ---------------------------------------------------------------------------

lint: ## Run flake8 and black check
	poetry run flake8 apps/ config/
	poetry run black --check apps/ config/

format: ## Auto-format code with black
	poetry run black apps/ config/

# ---------------------------------------------------------------------------
# Maintenance
# ---------------------------------------------------------------------------

clean: ## Remove Python cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

poetry-update: ## Update Poetry lock file
	poetry lock
	poetry install
