#!/usr/bin/env python3
"""
Setup script for Indian Stock Analysis Dashboard
Automatically installs dependencies and sets up the environment
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    
    try:
        # Create requirements.txt from template if it doesn't exist
        if not os.path.exists('requirements.txt'):
            if os.path.exists('requirements-template.txt'):
                with open('requirements-template.txt', 'r') as template:
                    content = template.read()
                with open('requirements.txt', 'w') as req_file:
                    req_file.write(content)
                print("✅ Created requirements.txt from template")
            else:
                # Create basic requirements.txt
                requirements = [
                    "streamlit>=1.42.0",
                    "pandas>=2.2.3", 
                    "numpy>=2.2.3",
                    "plotly>=6.0.0",
                    "yfinance>=0.2.52"
                ]
                with open('requirements.txt', 'w') as req_file:
                    req_file.write('\n'.join(requirements))
                print("✅ Created requirements.txt")
        
        # Install packages
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("✅ Dependencies installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def create_streamlit_config():
    """Create Streamlit configuration"""
    config_dir = '.streamlit'
    config_file = os.path.join(config_dir, 'config.toml')
    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    
    if not os.path.exists(config_file):
        config_content = """[theme]
primaryColor = "#00FF9D"
backgroundColor = "#1E1E1E"
secondaryBackgroundColor = "#2D2D2D"
textColor = "#FFFFFF"

[server]
headless = true
address = "localhost"
port = 8501
"""
        with open(config_file, 'w') as f:
            f.write(config_content)
        print("✅ Created Streamlit configuration")

def main():
    """Main setup function"""
    print("🔧 Setting up Indian Stock Analysis Dashboard...")
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create Streamlit config
    create_streamlit_config()
    
    print("\n🎉 Setup complete!")
    print("To start the dashboard, run: python run.py")
    print("Or directly: streamlit run main.py")

if __name__ == "__main__":
    main()