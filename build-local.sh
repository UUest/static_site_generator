#!/bin/bash

# Build script for local development (no basepath)
echo "Building site for local development..."

python3 src/main.py ""

echo "Site built successfully!"
echo "You can serve the docs/ directory with:"
echo "  cd docs && python3 -m http.server 8000"
echo "Then visit http://localhost:8000"
