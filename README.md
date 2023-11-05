# Cookiecutter Django

[![Build Status](https://img.shields.io/github/actions/workflow/status/cookiecutter/cookiecutter-django/ci.yml?branch=master)](https://github.com/cookiecutter/cookiecutter-django/actions/workflows/ci.yml?query=branch%3Amaster)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest)](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cookiecutter/cookiecutter-django/master.svg)](https://results.pre-commit.ci/latest/github/cookiecutter/cookiecutter-django/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Updates](https://pyup.io/repos/github/cookiecutter/cookiecutter-django/shield.svg)](https://pyup.io/repos/github/cookiecutter/cookiecutter-django/)
[![Join our Discord](https://img.shields.io/badge/Discord-cookiecutter-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/uFXweDQc5a)
[![Code Helpers Badge](https://www.codetriage.com/cookiecutter/cookiecutter-django/badges/users.svg)](https://www.codetriage.com/cookiecutter/cookiecutter-django)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Django is a framework for jumpstarting
production-ready Django projects quickly.

- Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
- See [Troubleshooting](https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html) for common errors and obstacles
- If you have problems with Cookiecutter Django, please open [issues](https://github.com/cookiecutter/cookiecutter-django/issues/new) don't send
  emails to the maintainers.

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
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default
- Backup management for database for pythonanywhere included(MySQL)

## Work in progress
- Media storage using Amazon S3, Google Cloud Storage, Azure Storage or nginx