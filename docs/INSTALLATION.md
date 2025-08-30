# 📦 Installation Guide

## Prerequisites

- **Python 3.11 or higher**
- **pip package manager**
- **Internet connection** (for stock data)

## Quick Installation

### Option 1: VS Code Workflow (Recommended)
```bash
# Clone or download the repository
git clone https://github.com/yourusername/indian-stock-dashboard.git
cd indian-stock-dashboard

# Install dependencies
pip install -r requirements.txt

# Run in VS Code terminal
streamlit run main.py
```

### Option 2: Automated Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/indian-stock-dashboard.git
cd indian-stock-dashboard

# Run automated setup
python setup.py

# Start the application
python run.py
```

### Option 2: Install from PyPI (if published)
```bash
pip install indian-stock-dashboard
streamlit run main.py
```

## Detailed Setup

### 1. System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.11 or higher
- **Memory**: At least 512MB RAM
- **Storage**: 50MB free space

### 2. Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv stock-dashboard-env

# Activate (Windows)
stock-dashboard-env\Scripts\activate

# Activate (macOS/Linux)
source stock-dashboard-env/bin/activate

# Copy requirements template and install dependencies
cp requirements-template.txt requirements.txt
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run main.py
```

The dashboard will open at `http://localhost:8501`

## Troubleshooting

### Common Issues

**ImportError: No module named 'streamlit'**
```bash
pip install streamlit
```

**ImportError: No module named 'yfinance'**
```bash
pip install yfinance
```

**Port 8501 is already in use**
```bash
streamlit run main.py --server.port 8502
```

**Yahoo Finance Rate Limiting**
- The app automatically switches to demo mode
- Wait 10-15 minutes and try again
- Use during off-peak hours for better performance

### Python Version Issues
If you have multiple Python versions:
```bash
python3.11 -m pip install streamlit pandas numpy plotly yfinance
python3.11 -m streamlit run main.py
```

## Configuration

### Custom Port
```bash
streamlit run main.py --server.port 8080
```

### Custom Address
```bash
streamlit run main.py --server.address 0.0.0.0
```

### Development Mode
```bash
streamlit run main.py --logger.level debug
```

## Docker Installation

### Build and Run
```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN cp requirements-template.txt requirements.txt && pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
EOF

# Build image
docker build -t indian-stock-dashboard .

# Run container
docker run -p 8501:8501 indian-stock-dashboard
```

## Deployment Options

### Streamlit Cloud
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository and deploy

### Heroku
```bash
# Create Procfile
echo "web: streamlit run main.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy to Heroku
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Railway
```bash
# Create railway.json
cat > railway.json << EOF
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run main.py --server.port=$PORT --server.address=0.0.0.0"
  }
}
EOF
```

## Verification

After installation, verify everything works:

1. **Check dependencies**:
   ```bash
   python -c "import streamlit, pandas, numpy, plotly, yfinance; print('All dependencies installed successfully!')"
   ```

2. **Test the application**:
   - Visit `http://localhost:8501`
   - Select a stock (e.g., RELIANCE.NS)
   - Click "Analyze Stock"
   - Verify charts and metrics display

3. **Test demo mode**:
   - If you see "Rate Limited" message, demo mode is working
   - Charts should show sample data
   - All tabs should be functional

## Performance Tips

- **Use SSD storage** for better file I/O performance
- **Close other browser tabs** to free up memory
- **Use Chrome or Firefox** for best compatibility
- **Enable hardware acceleration** in browser settings