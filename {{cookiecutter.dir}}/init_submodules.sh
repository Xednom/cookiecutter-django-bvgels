#!/bin/bash

# Script to initialize and update git submodules
echo "Initializing and updating git submodules..."

# Check if .gitmodules file exists
if [ ! -f .gitmodules ]; then
    echo "Error: No .gitmodules file found in the current directory."
    echo "This script should be run from the project root directory."
    exit 1
fi

# Initialize submodules
echo "Initializing submodules..."
git submodule init

# Update submodules to their latest commits
echo "Updating submodules..."
git submodule update

# Make sure submodules are on the correct branch
echo "Checking submodule branches..."
git submodule foreach 'git checkout $(git config -f $toplevel/.gitmodules submodule.$name.branch || echo main || echo master)'

echo "Git submodules have been successfully initialized and updated!"
echo "Submodules in this project:"
git submodule status
