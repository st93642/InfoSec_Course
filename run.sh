#!/usr/bin/env bash
set -euo pipefail

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies in venv
pip install -r requirements.txt

# Run the app
exec python main.py