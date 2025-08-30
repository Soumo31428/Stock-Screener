#!/bin/bash
# Unix/Linux/macOS shell script to start the Indian Stock Analysis Dashboard

echo "🚀 Starting Indian Stock Analysis Dashboard..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.11 or higher"
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $required_version or higher is required"
    echo "Current version: $python_version"
    exit 1
fi

# Run setup if first time
if [ ! -f "requirements.txt" ]; then
    echo "🔧 First time setup..."
    python3 setup.py
fi

# Start the dashboard
echo "🌟 Starting dashboard..."
python3 run.py