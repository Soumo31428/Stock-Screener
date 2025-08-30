# 🔌 API Documentation

## Overview

The Indian Stock Analysis Dashboard uses modular functions that can be imported and used independently. This document outlines the public API.

## Core Functions

### Data Retrieval

#### `get_stock_data(symbol, period='1y', start_date=None, end_date=None, retry_count=3)`

Fetch stock data from Yahoo Finance with intelligent retry logic.

**Parameters:**
- `symbol` (str): Stock symbol (e.g., 'RELIANCE.NS')
- `period` (str): Time period ('1mo', '3mo', '6mo', '1y', '2y', '5y', 'custom')
- `start_date` (str): Start date for custom period (YYYY-MM-DD)
- `end_date` (str): End date for custom period (YYYY-MM-DD)
- `retry_count` (int): Number of retry attempts (default: 3)

**Returns:**
- `tuple`: (hist_data, stock_info) or (None, error_code)

**Example:**
```python
from utils import get_stock_data

# Get 1 year data for Reliance
hist_data, stock_info = get_stock_data('RELIANCE.NS', '1y')

# Get custom date range
hist_data, stock_info = get_stock_data(
    'TCS.NS', 
    'custom', 
    '2024-01-01', 
    '2024-12-31'
)
```

#### `get_sample_stock_data(symbol, period='1y')`

Generate realistic sample data when Yahoo Finance is unavailable.

**Parameters:**
- `symbol` (str): Stock symbol
- `period` (str): Time period

**Returns:**
- `tuple`: (sample_hist_data, sample_stock_info)

**Example:**
```python
from utils import get_sample_stock_data

# Generate sample data
hist_data, stock_info = get_sample_stock_data('RELIANCE.NS', '6mo')
```

### Technical Analysis

#### `calculate_metrics(df)`

Calculate technical indicators for stock data.

**Parameters:**
- `df` (DataFrame): Stock price data with OHLCV columns

**Returns:**
- `DataFrame`: Original data with added technical indicators

**Added Columns:**
- `SMA_20`: 20-day Simple Moving Average
- `SMA_50`: 50-day Simple Moving Average
- `RSI`: Relative Strength Index
- `MACD`: MACD line
- `Signal_Line`: MACD signal line
- `BB_upper`: Bollinger Bands upper
- `BB_middle`: Bollinger Bands middle
- `BB_lower`: Bollinger Bands lower

**Example:**
```python
from utils import calculate_metrics, get_stock_data

hist_data, _ = get_stock_data('INFY.NS')
df_with_indicators = calculate_metrics(hist_data)

# Access indicators
rsi_values = df_with_indicators['RSI']
bollinger_upper = df_with_indicators['BB_upper']
```

#### `calculate_rsi(prices, period=14)`

Calculate Relative Strength Index.

**Parameters:**
- `prices` (Series): Price series
- `period` (int): RSI period (default: 14)

**Returns:**
- `Series`: RSI values

### Visualization

#### `create_price_chart(df, symbol, period='1y')`

Create interactive price chart with technical indicators.

**Parameters:**
- `df` (DataFrame): Stock data with technical indicators
- `symbol` (str): Stock symbol for chart title
- `period` (str): Time period for formatting

**Returns:**
- `plotly.graph_objects.Figure`: Interactive chart

**Example:**
```python
from utils import get_stock_data, calculate_metrics, create_price_chart
import streamlit as st

# Get data and create chart
hist_data, _ = get_stock_data('HDFC BANK.NS')
df = calculate_metrics(hist_data)
chart = create_price_chart(df, 'HDFCBANK.NS', '1y')

# Display in Streamlit
st.plotly_chart(chart, use_container_width=True)
```

### Data Formatting

#### `format_number(number)`

Format large numbers with K, M, B suffixes.

**Parameters:**
- `number` (float): Number to format

**Returns:**
- `str`: Formatted number string

**Example:**
```python
from utils import format_number

print(format_number(1500000))     # "1.50M"
print(format_number(2500000000))  # "2.50B"
print(format_number(750000))      # "750.00K"
```

#### `get_financial_metrics(info)`

Extract and format financial metrics from stock info.

**Parameters:**
- `info` (dict): Stock information dictionary

**Returns:**
- `dict`: Formatted financial metrics in rupees

**Example:**
```python
from utils import get_stock_data, get_financial_metrics

_, stock_info = get_stock_data('TCS.NS')
metrics = get_financial_metrics(stock_info)

print(metrics['Market Cap'])    # "₹12.50T"
print(metrics['P/E Ratio'])     # "28.5"
print(metrics['EPS (TTM)'])     # "₹125.30"
```

#### `get_company_profile(info)`

Extract company profile information.

**Parameters:**
- `info` (dict): Stock information dictionary

**Returns:**
- `dict`: Company profile data

**Example:**
```python
from utils import get_stock_data, get_company_profile

_, stock_info = get_stock_data('WIPRO.NS')
profile = get_company_profile(stock_info)

print(profile['Sector'])          # "Technology"
print(profile['Industry'])        # "Software"
print(profile['Full Time Employees'])  # "245,000"
```

## Constants

### Default Stock Universe

```python
DEFAULT_STOCKS = [
    'RELIANCE.NS',    # Reliance Industries
    'TCS.NS',         # Tata Consultancy Services
    'HDFCBANK.NS',    # HDFC Bank
    'INFY.NS',        # Infosys
    'ICICIBANK.NS',   # ICICI Bank
    'HINDUNILVR.NS',  # Hindustan Unilever
    'SBIN.NS',        # State Bank of India
    'BHARTIARTL.NS',  # Bharti Airtel
    'ITC.NS',         # ITC Limited
    'KOTAKBANK.NS',   # Kotak Mahindra Bank
    'LT.NS',          # Larsen & Toubro
    'BAJFINANCE.NS',  # Bajaj Finance
    'ASIANPAINT.NS',  # Asian Paints
    'MARUTI.NS',      # Maruti Suzuki
    'WIPRO.NS',       # Wipro
    'TITAN.NS',       # Titan Company
    'ADANIENT.NS',    # Adani Enterprises
    'ULTRACEMCO.NS',  # UltraTech Cement
    'SUNPHARMA.NS',   # Sun Pharma
    'AXISBANK.NS'     # Axis Bank
]
```

## Error Handling

### Error Codes

The API returns specific error codes for different failure scenarios:

- `"RATE_LIMITED"`: Yahoo Finance API rate limit exceeded
- `"NO_DATA"`: No data available for the symbol
- `"INCOMPLETE_INFO"`: Partial data received
- `"MAX_RETRIES_EXCEEDED"`: All retry attempts failed
- `"ERROR: {message}"`: Specific error with details

### Example Error Handling

```python
from utils import get_stock_data

hist_data, result = get_stock_data('INVALID.NS')

if hist_data is None:
    if result == "RATE_LIMITED":
        print("API rate limited. Switching to demo mode...")
        # Use get_sample_stock_data instead
    elif result == "NO_DATA":
        print("Invalid stock symbol")
    elif result.startswith("ERROR:"):
        print(f"Error occurred: {result}")
```

## Integration Examples

### Basic Stock Analysis

```python
import pandas as pd
from utils import get_stock_data, calculate_metrics, get_financial_metrics

def analyze_stock(symbol):
    # Get data
    hist_data, stock_info = get_stock_data(symbol)
    
    if hist_data is None:
        return None
    
    # Calculate indicators
    df = calculate_metrics(hist_data)
    
    # Get metrics
    metrics = get_financial_metrics(stock_info)
    
    # Basic analysis
    current_price = df['Close'].iloc[-1]
    rsi = df['RSI'].iloc[-1]
    
    return {
        'symbol': symbol,
        'current_price': current_price,
        'rsi': rsi,
        'pe_ratio': metrics['P/E Ratio'],
        'market_cap': metrics['Market Cap']
    }

# Example usage
result = analyze_stock('RELIANCE.NS')
print(result)
```

### Batch Processing

```python
from utils import get_stock_data, DEFAULT_STOCKS

def get_all_stock_prices():
    prices = {}
    
    for symbol in DEFAULT_STOCKS:
        hist_data, stock_info = get_stock_data(symbol, '1mo')
        
        if hist_data is not None:
            current_price = hist_data['Close'].iloc[-1]
            prices[symbol] = current_price
        else:
            prices[symbol] = None
    
    return prices

# Get current prices for all stocks
all_prices = get_all_stock_prices()
```

## Performance Considerations

- **Caching**: Consider implementing caching for repeated requests
- **Rate Limiting**: Be aware of Yahoo Finance API limits
- **Batch Requests**: Avoid making too many simultaneous requests
- **Error Handling**: Always handle potential API failures gracefully

## Version Compatibility

- **Python**: 3.11+
- **Pandas**: 2.2.3+
- **NumPy**: 2.2.3+
- **Plotly**: 6.0.0+
- **yfinance**: 0.2.52+