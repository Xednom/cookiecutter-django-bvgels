#!/usr/bin/env python
"""
Post-generation hook for cookiecutter-django-bvgels.
Runs automatically after the project is generated to set up the development environment.
"""

import os
import shutil
import subprocess
import sys


def run_command(command, description=None, check=True, cwd=None):
    """Run a shell command and print its output."""
    if description:
        print(f"\n{'='*60}")
        print(f"  {description}")
        print(f"{'='*60}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=check,
            capture_output=True,
            text=True,
            cwd=cwd,
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr and result.returncode != 0:
            print(result.stderr, file=sys.stderr)
        return result
    except subprocess.CalledProcessError as e:
        if check:
            print(f"Error running command: {command}", file=sys.stderr)
            print(f"Exit code: {e.returncode}", file=sys.stderr)
            print(f"Output: {e.output}", file=sys.stderr)
            sys.exit(1)
        return e


def main():
    project_dir = os.getcwd()
    print(f"\n🔧 Post-generation setup running in: {project_dir}")

    # --- 1. Initialize Git repository ---
    if not os.path.exists(os.path.join(project_dir, ".git")):
        run_command("git init", description="Initializing Git repository")
    else:
        print("\n   Git repository already initialized.")

    # --- 2. Initialize and update submodules ---
    gitmodules_path = os.path.join(project_dir, ".gitmodules")
    if os.path.exists(gitmodules_path):
        run_command("git submodule init", description="Initializing Git submodules")
        run_command("git submodule update", description="Updating Git submodules")
    else:
        print("\n   No .gitmodules file found. Skipping submodule initialization.")

    # --- 3. Create .env from env.example ---
    env_path = os.path.join(project_dir, ".env")
    env_example_path = os.path.join(project_dir, "env.example")
    if not os.path.exists(env_path) and os.path.exists(env_example_path):
        shutil.copy2(env_example_path, env_path)
        print("\n   .env file created from env.example.")
    elif os.path.exists(env_path):
        print("\n   .env file already exists.")
    else:
        print("\n   WARNING: env.example not found. Cannot create .env.")

    # --- 4. Check / install Poetry ---
    poetry_check = run_command(
        "poetry --version",
        description="Checking for Poetry",
        check=False,
    )
    if poetry_check.returncode != 0:
        print("\n   Poetry not found. Installing...")
        run_command("curl -sSL https://install.python-poetry.org | python3 -")
        poetry_bin = os.path.expanduser("~/.local/bin/poetry")
        if os.path.exists(poetry_bin):
            os.environ["PATH"] = os.path.expanduser("~/.local/bin") + os.pathsep + os.environ.get("PATH", "")
        else:
            print("   WARNING: Poetry was installed but not found in PATH. Please restart your shell.")
    else:
        print(f"\n   Found: {poetry_check.stdout.strip()}")

    # --- 5. Lock and install dependencies ---
    run_command("poetry lock --no-update", description="Locking Poetry dependencies")
    run_command("poetry install --no-root", description="Installing Poetry dependencies")

    # --- 6. Run migrations ---
    run_command(
        "poetry run python manage.py migrate",
        description="Applying database migrations",
        check=False,
    )

    # --- 7. Print success message ---
    print("\n" + "=" * 60)
    print("  ✅ Project setup complete!")
    print("=" * 60)
    print(f"""
📁 Project directory: {project_dir}

🚀 Quick start:
   cd {os.path.basename(project_dir)}
   make run                  # Run the Django development server
   make docker-up            # Run everything in Docker
   make migrate              # Run database migrations
   make test                 # Run the test suite

📖 Full documentation: https://cookiecutter-django.readthedocs.io/
""")


if __name__ == "__main__":
    main()
