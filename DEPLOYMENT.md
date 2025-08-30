# 🚀 Deployment Guide

## Local Development

### Windows Users
Double-click `start.bat` or run in Command Prompt:
```cmd
start.bat
```

### macOS/Linux Users
Run in Terminal:
```bash
./start.sh
```

### Cross-Platform
```bash
python setup.py  # First time only
python run.py    # Every time
```

## Cloud Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set main file: `main.py`
5. Deploy automatically

### Heroku Deployment
```bash
# Create Procfile
echo "web: streamlit run main.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Create runtime.txt
echo "python-3.11.0" > runtime.txt

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Railway Deployment
```bash
# Create railway.json
cat > railway.json << EOF
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run main.py --server.port=\$PORT --server.address=0.0.0.0"
  }
}
EOF
```

### Docker Deployment
```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install -r standalone-requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
EOF

# Build and run
docker build -t indian-stock-dashboard .
docker run -p 8501:8501 indian-stock-dashboard
```

## Environment Variables

### Optional Configuration
- `STREAMLIT_SERVER_PORT`: Custom port (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Custom address (default: localhost)

### Example
```bash
export STREAMLIT_SERVER_PORT=8080
python run.py
```

## Production Considerations

### Performance
- Use a production WSGI server for large deployments
- Enable caching for repeated API calls
- Consider rate limiting for Yahoo Finance API

### Security
- Run behind a reverse proxy (nginx)
- Use HTTPS in production
- Implement proper error logging

### Monitoring
- Monitor Yahoo Finance API usage
- Track application performance
- Set up health checks for deployments