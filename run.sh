#!/bin/bash

# LuckyWeaver - Local Run Script

echo "Starting LuckyWeaver..."
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Run app
echo "Starting application on http://localhost:5001"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 app.py
