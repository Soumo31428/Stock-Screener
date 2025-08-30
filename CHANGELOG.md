# 📝 Changelog

All notable changes to the Indian Stock Analysis Dashboard will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub showcase documentation
- Professional README with screenshots
- Contributing guidelines
- MIT License
- Feature overview documentation

## [1.0.0] - 2024-12-30

### Added
- Initial release of Indian Stock Analysis Dashboard
- Real-time stock data for 20 major Indian companies
- Interactive price charts with line visualization
- Technical indicators: RSI, MACD, Bollinger Bands
- Volume analysis with area charts
- Financial metrics in Indian Rupees (₹)
- Company profile information
- Smart rate limiting with demo mode
- Dark theme UI with green accents
- Multiple time period analysis (1mo to 5y)
- Custom date range selection
- Responsive design for mobile and desktop

### Features
- **Stock Universe**: 20 pre-selected Indian Fortune 500 companies
- **Chart Types**: Clean line charts instead of candlestick charts
- **Time Labels**: Dynamic hourly/daily labels based on period
- **Error Handling**: Comprehensive error messages with solutions
- **Demo Mode**: Realistic sample data when API is rate-limited
- **Currency**: All financial metrics displayed in Indian Rupees
- **Technical Analysis**: RSI, MACD, Bollinger Bands
- **Performance**: Under 1000 lines of code, 5 dependencies only

### Technical
- **Framework**: Streamlit for web interface
- **Data Source**: Yahoo Finance API via yfinance
- **Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas and NumPy
- **Architecture**: Minimalist design with 4 core files

## [0.9.0] - 2024-12-29

### Added
- Smart retry logic for API calls
- Exponential backoff for rate limiting
- Detailed error messaging system
- Alternative stock suggestions on errors

### Changed
- Improved error handling with specific error types
- Enhanced user experience with actionable solutions
- Better rate limiting communication

## [0.8.0] - 2024-12-29

### Added
- Dynamic time labeling system
- Hourly labels for periods ≤5 days
- Daily labels for periods >5 days
- Chart title updates based on time period

### Removed
- 20-day and 50-day moving averages from charts
- Cluttered technical indicators

### Changed
- Cleaner chart visualization
- Focus on essential price action

## [0.7.0] - 2024-12-29

### Changed
- Replaced candlestick charts with line charts
- Updated volume visualization to area charts
- All financial metrics now display in Indian Rupees (₹)
- Improved chart color scheme

### Added
- User preference documentation in replit.md
- Chart customization preferences

## [0.6.0] - 2024-12-29

### Added
- Comprehensive demo mode with realistic sample data
- Sample data generator for all 20 stocks
- Realistic price movements and volatility
- Complete dashboard functionality in demo mode

### Improved
- User experience during API rate limiting
- Clear demo mode notifications
- Seamless transition between real and sample data

## [0.5.0] - 2024-12-29

### Added
- Initial rate limiting detection
- Basic error handling for API failures
- Retry mechanism for failed requests

### Fixed
- Streamlit font configuration warnings
- CSS styling issues

## [0.4.0] - 2024-12-29

### Added
- Complete financial metrics system
- Company profile information
- News integration capabilities
- ESG scoring display

### Enhanced
- Financial data presentation
- Metric calculations and formatting
- Company information layout

## [0.3.0] - 2024-12-29

### Added
- Technical indicator calculations
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Moving averages (20-day and 50-day)

### Improved
- Chart visualization quality
- Technical analysis capabilities

## [0.2.0] - 2024-12-29

### Added
- Interactive Plotly charts
- Multi-panel chart layout
- Price, volume, and RSI visualization
- Dark theme integration

### Enhanced
- Chart performance and responsiveness
- Visual design consistency

## [0.1.0] - 2024-12-29

### Added
- Basic Streamlit application structure
- Yahoo Finance API integration
- Initial stock data fetching
- Basic UI layout and navigation
- 20 Indian stock symbols
- Time period selection
- Custom CSS styling

### Technical
- Project setup with pyproject.toml
- Streamlit configuration
- Basic error handling
- Session state management

---

## Legend

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements