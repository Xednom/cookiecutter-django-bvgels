# Cookiecutter Django

[![Build Status](https://img.shields.io/github/actions/workflow/status/cookiecutter/cookiecutter-django/ci.yml?branch=master)](https://github.com/cookiecutter/cookiecutter-django/actions/workflows/ci.yml?query=branch%3Amaster)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest)](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cookiecutter/cookiecutter-django/master.svg)](https://results.pre-commit.ci/latest/github/cookiecutter/cookiecutter-django/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Django is a framework for jumpstarting production-ready Django projects quickly.

- Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
- If you have problems with Cookiecutter Django, please open [issues](https://github.com/cookiecutter/cookiecutter-django/issues/new) don't send emails to the maintainers.

## Features

- For Django 4.2
- Works with Python 3.11
- Renders Django projects with REST Framework
- [12-Factor](https://12factor.net) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Registration via [djoser](https://github.com/sunscrapers/djoser)
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default)
- Backup management for database for pythonanywhere included (MySQL)
- **Docker Compose** ready (PostgreSQL + Django)
- **One-command setup** — run cookiecutter and everything is configured automatically
- **Makefile** with common development commands

## Work in progress

- **Media storage** — `django-storages` + `google-cloud-storage` included. Configuration examples:
  - **Google Cloud Storage** (recommended): Set `GS_BUCKET_NAME`, `GS_PROJECT_ID`, and credentials (`GOOGLE_CREDENTIALS_JSON`, `GOOGLE_CREDENTIALS_JSON_FILE`, or `GOOGLE_APPLICATION_CREDENTIALS`) in `.env`. Falls back to local filesystem when not configured.
  - **Amazon S3**: Set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`
  - **Azure Storage**: Set `AZURE_ACCOUNT_NAME`, `AZURE_CONTAINER`
  - **nginx + local files**: Serve media from a dedicated volume (works out of the box as fallback)

---

## Quick Start (One Command)

> **Prerequisites:** Python 3.11+, [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html), [Poetry](https://python-poetry.org/docs/#installation), and [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for Docker Compose).

Run cookiecutter. The post-generation hook will automatically:

1. Initialize a Git repository
2. Initialize and update Git submodules (`apps/django_bvgels`, `apps/authentication`)
3. Create `.env` from `env.example`
4. Install Poetry dependencies
5. Apply database migrations

```bash
cookiecutter gh:Xednom/cookiecutter-django-bvgels
```

After generation finishes, you can start developing immediately:

```bash
cd <your-project-name>
make run           # Django dev server on http://localhost:8000
make docker-up     # OR: run everything in Docker
```

---

## Makefile Commands

All common tasks are available via `make`:

| Command | Description |
|---------|-------------|
| `make setup` | Full setup (git, submodules, .env, poetry, migrate) |
| `make run` | Start Django development server |
| `make migrate` | Apply database migrations |
| `make makemigrations` | Create new database migrations |
| `make createsuperuser` | Create a Django superuser |
| `make test` | Run the test suite (pytest) |
| `make shell` | Open Django shell |
| `make docker-up` | Start Docker Compose services |
| `make docker-down` | Stop Docker Compose services |
| `make docker-logs` | Tail Docker Compose logs |
| `make docker-shell` | Open a shell inside the web container |
| `make docker-migrate` | Run migrations inside Docker |
| `make docker-test` | Run tests inside Docker |
| `make lint` | Run linting (flake8 + black --check) |
| `make format` | Auto-format code with black |
| `make clean` | Remove Python cache files |

Run `make help` to see all available commands.

---

## Docker Compose

The generated project includes a `docker-compose.yml` with two services:

- **db** — PostgreSQL 15 (data persisted in a Docker volume)
- **web** — Django app built from the included `Dockerfile`

The web service automatically runs `migrate` on startup and then starts `runserver` for development.

```bash
# Start everything (builds on first run)
make docker-up

# View logs
make docker-logs

# Run migrations manually inside the container
make docker-migrate

# Stop everything
make docker-down
```

### Dockerfile Targets

| Target | Purpose |
|--------|---------|
| `production` (default) | Runs Gunicorn with 3 workers |
| `builder` | Used internally to create the Poetry virtual environment |

The `docker-compose.yml` overrides the default CMD to run the Django development server with live-reload for convenience.

---

## Manual Setup (without post-gen hook)

If you skip the post-generation hook, you can set up the project manually:

```bash
cd <your-project-name>
git init                          # Initialize git repo
git submodule init               # Init submodules
git submodule update             # Pull submodule code
cp env.example .env              # Create environment file
poetry lock --no-update          # Lock dependencies
poetry install --no-root         # Install dependencies
poetry run python manage.py migrate  # Apply migrations
poetry run python manage.py runserver # Start dev server
```

---

## Platform Environments

The generated project uses `django-split-settings` with platform-specific overrides:

| Platform | File | Purpose |
|----------|------|---------|
| `local` | `config/settings/platform/local.py` | Development (DEBUG=True, CORS open) |
| `staging` | `config/settings/platform/staging.py` | Staging (DEBUG=False, SSL) |
| `qa` | `config/settings/platform/qa.py` | QA environment |
| `prod` | `config/settings/platform/prod.py` | Production (DEBUG=False, HSTS, secure cookies) |

Set the `PLATFORM` environment variable in your `.env` file:

```bash
PLATFORM=local
```

---

## Git Submodules

The generated project depends on two submodules:

- `apps/django_bvgels` — Core Django BVGELS functionality
- `apps/authentication` — Authentication system (custom User model, Djoser endpoints)

These are managed via Git submodules and are automatically initialized by the post-generation hook.

If you need to update submodules to the latest commit later:

```bash
make setup          # Re-runs submodule update
# OR
git submodule update --remote
```

---

## Deployment

### Railway

The generated project includes a `Dockerfile` ready for Railway deployment:

1. Push your project to GitHub (submodules included)
2. Connect your repo to [Railway](https://railway.app/)
3. Railway will build from the `Dockerfile` using the `production` target
4. Add a PostgreSQL database via Railway's plugins
5. Set environment variables (`DJANGO_SECRET_KEY`, `DATABASE_URL`, `PLATFORM=prod`, etc.)

### PythonAnywhere

A `config/backup.py` script is included for MySQL database backups on PythonAnywhere.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `poetry: command not found` | Run `curl -sSL https://install.python-poetry.org \| python3 -` and add `~/.local/bin` to your PATH |
| `psycopg2` build fails | Install `libpq-dev` (Debian/Ubuntu) or `postgresql-libs` (macOS) |
| Submodules empty | Run `make setup` or `git submodule update --init --recursive` |
| Port 5432 already in use | Stop local PostgreSQL or change the port in `docker-compose.yml` |

---

## Contributing

If you find bugs or have suggestions, please open an issue on GitHub.

---

## License

MIT License. See [LICENSE](https://github.com/Xednom/cookiecutter-django-bvgels/blob/master/LICENSE) for details.
