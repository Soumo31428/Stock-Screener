# 💻 VS Code Setup Guide

## Quick Start in VS Code

1. **Clone or Download**
   ```bash
   git clone https://github.com/yourusername/indian-stock-dashboard.git
   ```

2. **Open in VS Code**
   - File → Open Folder → Select `indian-stock-dashboard`

3. **Install Dependencies**
   - Open VS Code terminal (`Ctrl+`` ` or View → Terminal)
   - Run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Dashboard**
   ```bash
   streamlit run main.py
   ```

5. **Access Dashboard**
   - Browser opens automatically at `http://localhost:8501`
   - Or click the link in terminal

## VS Code Features Included

### Debugging Support
- Press `F5` to run with debugger
- Or use "Run Streamlit Dashboard" configuration

### Python Setup
- Automatic Python interpreter detection
- Code formatting with Black (optional)
- Linting with flake8 (optional)

### Terminal Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run main.py

# Run with custom port
streamlit run main.py --server.port 8080

# Run in development mode
streamlit run main.py --logger.level debug
```

## Recommended VS Code Extensions

### Essential
- **Python** (Microsoft) - Python language support
- **Pylance** (Microsoft) - Enhanced Python IntelliSense

### Optional
- **autoDocstring** - Generate docstrings
- **Black Formatter** - Code formatting
- **GitLens** - Enhanced Git capabilities
- **Material Icon Theme** - Better file icons

## Project Structure in VS Code

```
indian-stock-dashboard/
├── .vscode/                    # VS Code settings
│   ├── settings.json          # Editor preferences
│   └── launch.json            # Debug configuration
├── main.py                    # Main application (open first)
├── utils.py                   # Business logic
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

## Troubleshooting

### Python Not Found
1. Install Python 3.11+ from [python.org](https://python.org)
2. Restart VS Code
3. Select interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"

### Module Import Errors
```bash
# Ensure you're in the project directory
cd indian-stock-dashboard
pip install -r requirements.txt
```

### Port Already in Use
```bash
# Use different port
streamlit run main.py --server.port 8502
```

### Streamlit Not Starting
```bash
# Check if streamlit is installed
streamlit --version

# Reinstall if needed
pip install --upgrade streamlit
```

## Development Workflow

1. **Edit Code**: Modify `main.py` or `utils.py`
2. **Auto-Reload**: Streamlit automatically reloads on file changes
3. **Debug**: Use VS Code debugger or print statements
4. **Test**: Try different stocks and time periods
5. **Git**: Commit changes regularly

## Keyboard Shortcuts

- `Ctrl+`` ` - Open terminal
- `F5` - Start debugging
- `Ctrl+Shift+P` - Command palette
- `Ctrl+S` - Save and auto-format
- `Ctrl+/` - Toggle comment

## Performance Tips

- **Use virtual environment** for isolated dependencies
- **Close unused browser tabs** for better performance
- **Monitor terminal** for error messages
- **Check network** if Yahoo Finance data fails