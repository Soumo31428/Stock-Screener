# 📈 Indian Stock Analysis Dashboard

A modern, real-time stock analysis dashboard for Indian stock market built with Streamlit. Features intelligent rate-limiting handling with demo mode, interactive charts, and comprehensive financial metrics.

![Dashboard Preview](https://via.placeholder.com/800x400/1E1E1E/00FF9D?text=Stock+Analysis+Dashboard)

## ✨ Features

### 📊 **Smart Data Handling**
- **Real-time Analysis**: Live Indian stock data via Yahoo Finance API
- **Intelligent Fallback**: Automatic demo mode when rate-limited
- **20 Pre-loaded Stocks**: Major Indian companies (Reliance, TCS, HDFC Bank, etc.)

### 📈 **Interactive Visualizations**
- **Clean Line Charts**: Easy-to-read price trends (no cluttered candlesticks)
- **Dynamic Time Labels**: Hourly for short periods, daily for longer periods
- **Technical Indicators**: RSI, MACD, Bollinger Bands
- **Volume Analysis**: Smooth area charts with gradient fills

### 💰 **Financial Intelligence**
- **Complete Metrics**: P/E Ratio, Market Cap, EPS, ROE, Debt-to-Equity
- **Indian Currency**: All values displayed in Rupees (₹)
- **Company Profiles**: Sector, industry, employee count, business summary

### 🎯 **User Experience**
- **Dark Theme**: Professional interface with green accents
- **Responsive Design**: Works on desktop and mobile
- **Smart Error Handling**: Clear messages with actionable solutions
- **Multiple Time Periods**: 1 month to 5 years + custom date ranges

## 🚀 Live Demo

When Yahoo Finance API is rate-limited, the app automatically switches to demo mode with realistic sample data, maintaining full functionality.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Source**: yfinance (Yahoo Finance API)
- **Visualization**: Plotly (Interactive charts)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Ready for Streamlit Cloud, Heroku, or any Python hosting

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- pip package manager

### Quick Start (VS Code)
```bash
# Clone the repository
git clone https://github.com/yourusername/indian-stock-dashboard.git
cd indian-stock-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run main.py
```

### Alternative Methods
```bash
# Automated setup
python setup.py && python run.py

# Or double-click start.bat (Windows) / run ./start.sh (macOS/Linux)
```

The dashboard will open at `http://localhost:8501`

## 🏗️ Project Structure

```
indian-stock-dashboard/
├── main.py                     # Main Streamlit application
├── utils.py                    # Data processing & chart generation
├── run.py                      # Application launcher
├── setup.py                    # Automated setup script
├── requirements.txt            # Python dependencies
├── .vscode/                    # VS Code configuration
│   ├── settings.json          # Editor settings
│   └── launch.json            # Debug configuration
├── .streamlit/
│   └── config.toml            # Streamlit configuration (auto-generated)
├── docs/                      # Documentation folder
│   ├── INSTALLATION.md        # Installation guide
│   └── API.md                # API documentation
├── pyproject.toml             # Project metadata
└── README.md                  # This file
```

**Minimalist Design**: Standalone setup, cross-platform compatibility, 5 dependencies only.

## 🎨 Screenshots

### Main Dashboard
![Main Dashboard](https://via.placeholder.com/800x400/1E1E1E/00FF9D?text=Main+Dashboard+View)

### Interactive Charts
![Charts](https://via.placeholder.com/800x400/1E1E1E/FFB84D?text=Interactive+Price+Charts)

### Financial Metrics
![Metrics](https://via.placeholder.com/800x400/1E1E1E/4BFF4B?text=Financial+Metrics+in+Rupees)

### Demo Mode
![Demo Mode](https://via.placeholder.com/800x400/1E1E1E/FF4B4B?text=Smart+Demo+Mode)

## 📋 Usage Examples

### Analyzing a Stock
1. Select a stock from the sidebar dropdown (e.g., "RELIANCE.NS")
2. Choose time period (1mo, 3mo, 6mo, 1y, 2y, 5y)
3. Click "Analyze Stock" to view detailed analysis
4. Explore tabs: Price Charts, Company Profile, Financial Metrics, News

### Custom Date Ranges
1. Select "Custom" from time period dropdown
2. Set start and end dates using date pickers
3. Analyze specific market periods or events

### Demo Mode Experience
When Yahoo Finance rate limits requests, the app automatically:
- Shows realistic sample data for all 20 stocks
- Maintains full functionality including charts and metrics
- Displays clear notifications about demo mode
- Suggests when to retry for real data

## 🔧 Configuration

### Streamlit Settings
The app includes optimized settings in `.streamlit/config.toml`:
- Dark theme with green primary color
- Server configuration for production deployment
- Performance optimizations

### Customization Options
- **Stock Universe**: Modify `default_stocks` list in `main.py`
- **Chart Colors**: Update color schemes in `utils.py`
- **Styling**: Modify embedded CSS in `main.py`

## 🚦 API Rate Limiting

The dashboard intelligently handles Yahoo Finance API limitations:

- **Automatic Retries**: 3 attempts with exponential backoff
- **Smart Demo Mode**: Realistic sample data when rate-limited
- **Clear Messaging**: Users understand what's happening and when to retry
- **Full Functionality**: All features work even in demo mode

## 🌐 Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Heroku
```bash
# Add Procfile with: web: sh setup.sh && streamlit run main.py
echo "web: streamlit run main.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN cp requirements-template.txt requirements.txt && pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with clear description

### Areas for Enhancement
- [ ] Additional technical indicators (MACD histogram, Stochastic)
- [ ] Portfolio tracking and comparison features
- [ ] Export functionality for charts and data
- [ ] Mobile app version
- [ ] Integration with additional data sources

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Yahoo Finance**: Financial data provider
- **Streamlit Team**: Amazing web framework
- **Plotly**: Interactive visualization library
- **Indian Stock Exchanges**: NSE/BSE for market data

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

⭐ **Star this repository if you found it helpful!**

*Built with ❤️ for the Indian stock market community*