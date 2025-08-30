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

### Application Structure
- **main.py**: Primary Streamlit application with page configuration and session state management
- **app.py**: Alternative Taipy-based interface (appears incomplete)
- **utils.py**: Core business logic including data fetching, metric calculations, and chart creation
- **styles.css**: Custom styling with dark theme and responsive design

### Key Features
- **Real-time Analysis**: Live stock price tracking with 24-hour change indicators
- **Technical Indicators**: RSI, MACD, Bollinger Bands, and moving averages
- **Time Period Flexibility**: Support for predefined periods (1mo to 5y) and custom date ranges
- **Company Intelligence**: Company profiles, ESG scores, and financial metrics
- **News Integration**: Stock-specific news using web scraping

### Session Management
- Streamlit session state for maintaining user selections and navigation state
- Custom page routing system for different analysis views
- Persistent date range selections for custom analysis periods

## External Dependencies

### Market Data Services
- **yfinance**: Primary source for Indian stock market data, company information, and historical prices
- **Yahoo Finance API**: Underlying data source accessed through yfinance library

### Web Scraping
- **trafilatura**: Used for extracting and processing stock-related news content from web sources

### Visualization and UI
- **Plotly**: Interactive charting library for technical analysis visualizations
- **Streamlit**: Web application framework for the dashboard interface
- **Taipy**: Alternative GUI framework (partially implemented)

### Data Processing
- **Pandas**: Data manipulation and analysis library
- **NumPy**: Numerical computing for technical indicator calculations

### Frontend Assets
- **Google Fonts**: Inter and Roboto Mono fonts for typography
- **Custom CSS**: Dark theme styling with hover effects and responsive design

### Configuration
- **Streamlit Config**: Custom configuration in .streamlit/config.toml for application settings