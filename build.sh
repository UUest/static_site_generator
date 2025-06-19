#!/bin/bash

# Build script for GitHub Pages deployment
# This script generates the static site with the correct basepath for GitHub Pages
#
# The basepath should match your GitHub repository name
# Example: for repository "username/static_site_generator", use "/static_site_generator"
#
# For local development, use build-local.sh instead

echo "Building site for GitHub Pages deployment..."

python3 src/main.py "/static_site_generator"

echo "Site built successfully!"
echo "The generated files in docs/ are ready for GitHub Pages deployment."
