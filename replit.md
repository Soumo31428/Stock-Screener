# Indian Stock Analysis Dashboard

## Overview

This is a comprehensive stock analysis dashboard focused on Indian stocks, built primarily with Streamlit for web interface and yfinance for real-time market data. The application provides technical analysis, company profiles, financial metrics, and news for Indian Fortune 500 companies. The dashboard features interactive visualizations using Plotly and supports both predefined time periods and custom date ranges for analysis.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Primary Framework**: Streamlit for the main web interface with custom CSS styling
- **Secondary Framework**: Taipy GUI (partially implemented in app.py, appears to be an alternative interface)
- **Visualization**: Plotly for interactive charts and technical analysis graphs
- **Styling**: Custom CSS with dark theme, Google Fonts (Inter, Roboto Mono), and responsive design

### Data Processing Layer
- **Stock Data Source**: yfinance library for real-time Indian stock market data (.NS suffix)
- **Technical Analysis**: Custom calculations for RSI, MACD, Bollinger Bands, and moving averages
- **Data Manipulation**: Pandas and NumPy for data processing and mathematical operations
- **Default Stock Universe**: Predefined list of 20 Indian Fortune 500 companies (Reliance, TCS, HDFC Bank, etc.)

### Application Structure - Minimized
- **main.py**: Complete Streamlit application with embedded CSS styling and page management
- **utils.py**: Core business logic including data fetching, metric calculations, and chart creation
- **app.py**: Removed (Taipy alternative interface)
- **styles.css**: Removed (CSS embedded directly in main.py)

### Key Features
- **Real-time Analysis**: Live stock price tracking with 24-hour change indicators
- **Technical Indicators**: RSI, MACD, Bollinger Bands, and moving averages
- **Time Period Flexibility**: Support for predefined periods (1mo to 5y) and custom date ranges
- **Company Intelligence**: Company profiles, ESG scores, and financial metrics
- **News Integration**: Simplified news functionality (web scraping removed)

### Session Management
- Streamlit session state for maintaining user selections and navigation state
- Custom page routing system for different analysis views
- Persistent date range selections for custom analysis periods

## External Dependencies - Minimized

### Core Dependencies (5 packages only)
- **streamlit**: Web application framework for the dashboard interface  
- **yfinance**: Primary source for Indian stock market data and company information
- **pandas**: Data manipulation and analysis library
- **numpy**: Numerical computing for technical indicator calculations
- **plotly**: Interactive charting library for technical analysis visualizations

### Removed Dependencies
- **trafilatura**: Removed web scraping, simplified news functionality
- **taipy**: Removed alternative GUI framework and dependencies

### Frontend Assets - Embedded
- **CSS**: Dark theme styling embedded directly in main.py (no external files)
- **Configuration**: Minimal .streamlit/config.toml for server settings

### File Structure - Minimized
- **Total Dependencies**: 5 packages (reduced from 6+)
- **Total Core Files**: 4 files (reduced from 8+)
- **Code Size**: Under 1000 lines total
- **Removed Files**: app.py, styles.css