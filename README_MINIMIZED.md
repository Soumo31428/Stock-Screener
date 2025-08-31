# Indian Stock Analysis Dashboard - Minimized

A lightweight stock analysis dashboard for Indian stocks with smart rate-limiting handling.

## Key Features
- Real-time Indian stock analysis with fallback demo mode
- Interactive technical charts (RSI, MACD, Bollinger Bands)
- Company profiles and financial metrics
- Smart Yahoo Finance rate limit handling


## Dependencies (Only 5 packages)
```
streamlit    # Web framework
pandas       # Data processing  
numpy        # Calculations
plotly       # Interactive charts
yfinance     # Stock data
```

## Installation & Run
```bash
pip install streamlit pandas numpy plotly yfinance
streamlit run main.py
```

## Demo Mode
When Yahoo Finance rate limits requests, the app automatically switches to realistic sample data, maintaining full functionality.

## File Sizes
- main.py: ~400 lines (includes embedded CSS)
- utils.py: ~430 lines  
- Total: Under 1000 lines of code
- Dependencies: 5 packages only