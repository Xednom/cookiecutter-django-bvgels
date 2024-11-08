# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

[![Built with Cookiecutter Djangos Bvgels](https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Bvgels-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Deployment

We use [railway](https://railway.app/) for our deployment

# Generate secret key

- To generate a **secret key** and replace the existing one from the env.example, use this command:

      $ python manage.py generate_secret_key