#!/usr/bin/env python3
"""
Launcher script for Indian Stock Analysis Dashboard
Run this file to start the application: python run.py
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pandas', 'numpy', 'plotly', 'yfinance']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:", ', '.join(missing_packages))
        print("Please install them with: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("🚀 Starting Indian Stock Analysis Dashboard...")
    
    # Check if dependencies are installed
    if not check_dependencies():
        sys.exit(1)
    
    # Start Streamlit app
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'main.py',
            '--server.port=8501',
            '--server.address=localhost'
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()