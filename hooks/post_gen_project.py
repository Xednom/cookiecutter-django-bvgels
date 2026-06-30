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
    submodules_ok = True
    gitmodules_path = os.path.join(project_dir, ".gitmodules")
    if os.path.exists(gitmodules_path):
        run_command("git submodule init", description="Initializing Git submodules")
        run_command("git submodule update", description="Updating Git submodules")

        # Check if submodules have actual content (not just empty directories)
        submodule_dirs = ["apps/django_bvgels", "apps/authentication"]
        empty_submodules = []
        for subdir in submodule_dirs:
            full_path = os.path.join(project_dir, subdir)
            if not os.path.isdir(full_path) or not os.listdir(full_path):
                empty_submodules.append(subdir)

        if empty_submodules:
            submodules_ok = False
            print(f"\n   ⚠️  Submodules are empty: {', '.join(empty_submodules)}")
            print("   Migrations will be skipped.")
            print("   Populate the submodules, then run: make migrate")
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
    # Try lock --no-update first; if it fails (e.g. stale lock), fall back to full lock
    lock_result = run_command("poetry lock --no-update", description="Locking Poetry dependencies", check=False)
    if lock_result.returncode != 0:
        print("   Lock with --no-update failed. Retrying with full lock...")
        lock_result = run_command("poetry lock", description="Retrying Poetry lock (full)", check=False)
        if lock_result.returncode != 0:
            print("   WARNING: poetry lock failed. You may need to run 'poetry lock' manually.")

    # Try install --no-root first; if it fails, try full install
    install_result = run_command("poetry install --no-root", description="Installing Poetry dependencies", check=False)
    if install_result.returncode != 0:
        print("   Install with --no-root failed. Retrying with full install...")
        install_result = run_command("poetry install", description="Retrying Poetry install (full)", check=False)
        if install_result.returncode != 0:
            print("   WARNING: poetry install failed. You may need to run 'poetry install' manually.")

    # --- 6. Optional: install Google Cloud Storage backend ---
    # This is intentionally non-fatal; the project falls back to local filesystem storage
    # if google-cloud-storage can't be resolved (e.g. very new Python versions).
    run_command(
        "poetry add google-cloud-storage",
        description="Installing Google Cloud Storage backend (optional)",
        check=False,
    )

    # --- 7. Run migrations ---
    if submodules_ok:
        migrate_result = run_command(
            "poetry run python manage.py migrate",
            description="Applying database migrations",
            check=False,
        )
        if migrate_result.returncode != 0:
            print("\n   WARNING: migrations failed. This is normal if the database is not yet running.")
            print("   Run 'make migrate' or 'make docker-up' after starting the database.")
    else:
        print("\n   ⏭️  Skipping migrations because submodules are empty.")
        print("   Run 'make migrate' after populating submodules.")

    # --- 8. Print success message ---
    print("\n" + "=" * 60)
    print("  ✅ Project setup complete!")
    print("=" * 60)
    print(f"""
📁 Project directory: {project_dir}

🚀 Quick start:
   cd {os.path.basename(project_dir)}
   make run                  # Run the Django development server
   make docker-up            # Run everything in Docker (includes DB)
   make migrate              # Run database migrations
   make test                 # Run the test suite

📖 Full documentation: https://cookiecutter-django.readthedocs.io/
""")


if __name__ == "__main__":
    main()
