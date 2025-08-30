# 🤝 Contributing to Indian Stock Analysis Dashboard

Thank you for your interest in contributing! This guide will help you get started.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/indian-stock-dashboard.git
   cd indian-stock-dashboard
   ```
3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies**
   ```bash
   cp requirements-template.txt requirements.txt
   pip install -r requirements.txt
   ```
5. **Run the application**
   ```bash
   streamlit run main.py
   ```

## 🛠️ Development Guidelines

### Code Style
- **Python**: Follow PEP 8 guidelines
- **Functions**: Use descriptive names and docstrings
- **Comments**: Explain complex logic and business rules
- **Imports**: Group standard library, third-party, and local imports

### File Organization
- **main.py**: Streamlit UI and navigation logic
- **utils.py**: Data processing, calculations, and chart generation
- **Keep it minimal**: Avoid creating unnecessary files

### Testing Your Changes
Before submitting a pull request:

1. **Test with real data**: Ensure functionality works with live Yahoo Finance API
2. **Test demo mode**: Verify fallback behavior when rate-limited
3. **Test all time periods**: Check 1mo, 3mo, 6mo, 1y, 2y, 5y, and custom ranges
4. **Test all stocks**: Verify functionality across different Indian stocks
5. **Mobile responsiveness**: Check on different screen sizes

## 📝 Pull Request Process

### Before Submitting
- [ ] Test all functionality thoroughly
- [ ] Ensure code follows project conventions
- [ ] Update documentation if needed
- [ ] Add comments for complex logic

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested with real Yahoo Finance data
- [ ] Tested demo mode functionality
- [ ] Tested on multiple stocks and time periods
- [ ] Verified mobile responsiveness

## Screenshots (if applicable)
Add screenshots showing the changes
```

## 🐛 Reporting Issues

### Bug Reports
Please include:
- **Description**: Clear description of the bug
- **Steps to reproduce**: How to recreate the issue
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, browser
- **Screenshots**: If applicable

### Feature Requests
Please include:
- **Problem**: What problem does this solve?
- **Solution**: Describe your proposed solution
- **Alternatives**: Other approaches considered
- **Use case**: How would this benefit users?

## 🎯 Areas for Contribution

### High Priority
- [ ] **Additional Technical Indicators**
  - MACD Histogram
  - Stochastic Oscillator
  - Williams %R
  - Commodity Channel Index

- [ ] **Performance Improvements**
  - Data caching mechanisms
  - Faster chart rendering
  - Optimized API calls

- [ ] **User Experience**
  - Export functionality (PNG, PDF, CSV)
  - Dark/light theme toggle
  - Keyboard shortcuts

### Medium Priority
- [ ] **Portfolio Features**
  - Multiple stock comparison
  - Portfolio tracking
  - Performance analytics

- [ ] **Data Enhancement**
  - Historical news integration
  - Earnings calendar
  - Dividend tracking

### Low Priority
- [ ] **Mobile App**
  - React Native version
  - Flutter implementation

- [ ] **Advanced Analytics**
  - Machine learning predictions
  - Sentiment analysis
  - Risk assessment tools

## 🔧 Technical Architecture

### Key Components
- **Data Layer**: `utils.py` handles all data fetching and processing
- **UI Layer**: `main.py` manages Streamlit interface and user interactions
- **Configuration**: `.streamlit/config.toml` for app settings

### Design Principles
- **Minimalism**: Keep codebase small and focused
- **Reliability**: Graceful handling of API failures
- **Performance**: Fast loading and responsive UI
- **User-friendly**: Clear error messages and intuitive navigation

### Code Organization
```python
# utils.py structure
def get_stock_data()      # API calls and data fetching
def calculate_metrics()   # Technical indicator calculations  
def create_price_chart()  # Chart generation
def format_number()       # Data formatting utilities
def get_financial_metrics() # Financial calculations

# main.py structure
# Page configuration and CSS
# Stock selection and navigation
# Analysis display logic
# Error handling and demo mode
```

## 🧪 Testing Guidelines

### Manual Testing Checklist
- [ ] App starts without errors
- [ ] All 20 stocks load properly
- [ ] Charts display correctly
- [ ] Financial metrics show in rupees
- [ ] Demo mode activates when rate-limited
- [ ] All time periods work
- [ ] Custom date ranges function
- [ ] Mobile interface is responsive

### API Testing
- [ ] Test during market hours
- [ ] Test during off-market hours
- [ ] Test with invalid stock symbols
- [ ] Test with network connectivity issues
- [ ] Test rate limiting scenarios

## 📚 Resources

### Streamlit Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly in Streamlit](https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart)

### Financial Data
- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Yahoo Finance API](https://rapidapi.com/blog/how-to-use-the-yahoo-finance-api/)

### Indian Stock Market
- [NSE India](https://www.nseindia.com/)
- [BSE India](https://www.bseindia.com/)

## 🙋‍♀️ Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Email**: your.email@example.com

## 🏆 Recognition

Contributors will be recognized in:
- README.md acknowledgments
- CONTRIBUTORS.md file
- Release notes for significant contributions

---

Thank you for contributing to the Indian Stock Analysis Dashboard! 🚀