import streamlit as st
import pandas as pd
from utils import get_stock_data, get_sample_stock_data, calculate_metrics, create_price_chart, format_number, get_stock_news, get_company_profile, get_financial_metrics
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Embedded CSS styles
st.markdown("""
<style>
.stApp {
    background-color: #1E1E1E;
}

.stock-metric {
    font-family: 'monospace';
    font-size: 1.2rem;
    margin-bottom: 8px;
}

.indicator-up {
    color: #4BFF4B;
}

.indicator-down {
    color: #FF4B4B;
}

.css-1d391kg {
    background-color: #2D2D2D;
    border-radius: 8px;
    padding: 16px;
    margin: 16px 0;
    transition: all 300ms ease;
}

.css-1d391kg:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.news-item {
    background-color: #2D2D2D;
    padding: 12px;
    border-radius: 8px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

# Indian Fortune 500 stocks
default_stocks = [
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

# Initialize session state variables
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_stock' not in st.session_state:
    st.session_state.selected_stock = None
if 'custom_start_date' not in st.session_state:
    st.session_state.custom_start_date = datetime.now() - timedelta(days=365)
if 'custom_end_date' not in st.session_state:
    st.session_state.custom_end_date = datetime.now()

def show_analysis(selected_stock, time_period):
    """Show the analysis page content"""
    st.title(f"📈 {selected_stock} Analysis")

    # Load data
    with st.spinner('Loading stock data...'):
        if time_period == 'custom':
            start_date = st.session_state.custom_start_date.strftime('%Y-%m-%d')
            end_date = st.session_state.custom_end_date.strftime('%Y-%m-%d')
            hist_data, stock_info = get_stock_data(selected_stock, 'custom', start_date, end_date)
        else:
            hist_data, stock_info = get_stock_data(selected_stock, time_period)

        if hist_data is not None and stock_info is not None and stock_info not in ["NO_DATA", "INCOMPLETE_INFO", "RATE_LIMITED", "MAX_RETRIES_EXCEEDED"] and not str(stock_info).startswith("ERROR:"):
            # Calculate metrics
            df = calculate_metrics(hist_data)

            # Create tabs for different sections
            tab1, tab2, tab3, tab4 = st.tabs([
                "📊 Price & Technical Analysis",
                "🏢 Company Profile",
                "💰 Financial Metrics",
                "📰 News"
            ])

            with tab1:
                # Technical Analysis Chart
                st.plotly_chart(create_price_chart(df, selected_stock), use_container_width=True)

                # Summary metrics in a single row
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.markdown(f"""
                    <div class="stock-metric">
                        Current Price
                        <br/>
                        <span class="indicator-up">₹{format_number(stock_info.get('currentPrice', 0))}</span>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    change = stock_info.get('regularMarketChangePercent', 0)
                    indicator_class = "indicator-up" if change >= 0 else "indicator-down"
                    st.markdown(f"""
                    <div class="stock-metric">
                        24h Change
                        <br/>
                        <span class="{indicator_class}">{change:.2f}%</span>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="stock-metric">
                        52 Week High
                        <br/>
                        <span>₹{format_number(stock_info.get('fiftyTwoWeekHigh', 0))}</span>
                    </div>
                    """, unsafe_allow_html=True)

                with col4:
                    st.markdown(f"""
                    <div class="stock-metric">
                        52 Week Low
                        <br/>
                        <span>₹{format_number(stock_info.get('fiftyTwoWeekLow', 0))}</span>
                    </div>
                    """, unsafe_allow_html=True)

                # Add Market Status Indicator
                market_status = "Open" if stock_info.get('regularMarketOpen', None) else "Closed"
                status_color = "#4BFF4B" if market_status == "Open" else "#FF4B4B"
                st.markdown(f"""
                <div style='text-align: right; margin-top: 20px;'>
                    <span style='background-color: {status_color}; padding: 5px 10px; border-radius: 4px;'>
                        Market {market_status}
                    </span>
                </div>
                """, unsafe_allow_html=True)

            with tab2:
                # Company Profile with enhanced information
                company_profile = get_company_profile(stock_info)

                st.subheader("Company Overview")
                st.write(company_profile['Business Summary'])

                # Enhanced company metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("### Industry Information")
                    st.markdown(f"""
                    - **Sector**: {company_profile['Sector']}
                    - **Industry**: {company_profile['Industry']}
                    - **Employees**: {company_profile['Full Time Employees']}
                    """)

                with col2:
                    st.markdown("### Trading Information")
                    st.markdown(f"""
                    - **Exchange**: {stock_info.get('exchange', 'N/A')}
                    - **Currency**: {stock_info.get('currency', 'N/A')}
                    - **Market Cap**: ₹{format_number(stock_info.get('marketCap', 0))}
                    """)

                with col3:
                    st.markdown("### Key Dates")
                    st.markdown(f"""
                    - **Earnings Date**: {stock_info.get('earningsDate', ['N/A'])[0] if stock_info.get('earningsDate') else 'N/A'}
                    - **Ex-Dividend Date**: {stock_info.get('exDividendDate', 'N/A')}
                    - **Fiscal Year End**: {stock_info.get('lastFiscalYearEnd', 'N/A')}
                    """)

                # Company contact information
                st.subheader("Company Contact")
                col1, col2 = st.columns(2)
                with col1:
                    if company_profile['Website'] != 'N/A':
                        st.markdown(f"🌐 [Official Website]({company_profile['Website']})")
                    else:
                        st.write("Website not available")

                with col2:
                    st.markdown(f"📍 **Headquarters**: {stock_info.get('city', 'N/A')}, {stock_info.get('country', 'N/A')}")

                # Add sustainability score if available
                if stock_info.get('sustainabilityScore'):
                    st.subheader("ESG Scores")
                    esg_col1, esg_col2, esg_col3 = st.columns(3)
                    with esg_col1:
                        st.metric("Environmental Score", stock_info.get('environmentScore', 'N/A'))
                    with esg_col2:
                        st.metric("Social Score", stock_info.get('socialScore', 'N/A'))
                    with esg_col3:
                        st.metric("Governance Score", stock_info.get('governanceScore', 'N/A'))

            with tab3:
                # Financial Metrics
                financial_metrics = get_financial_metrics(stock_info)

                # Valuation Metrics
                st.subheader("Valuation Metrics")
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Market Cap", financial_metrics['Market Cap'])
                    st.metric("P/E Ratio", financial_metrics['P/E Ratio'])
                    st.metric("EPS (TTM)", financial_metrics['EPS (TTM)'])

                with col2:
                    st.metric("Revenue (TTM)", financial_metrics['Revenue (TTM)'])
                    st.metric("Profit Margin", financial_metrics['Profit Margin'])
                    st.metric("Operating Margin", financial_metrics['Operating Margin'])

                with col3:
                    st.metric("ROE", financial_metrics['ROE'])
                    st.metric("Beta", financial_metrics['Beta'])
                    st.metric("Dividend Yield", financial_metrics['Dividend Yield'])

                # Additional Financial Ratios
                st.subheader("Financial Ratios")
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Debt to Equity", financial_metrics['Debt to Equity'])

                with col2:
                    st.metric("Current Ratio", financial_metrics['Current Ratio'])

            with tab4:
                # News Section
                news_df = get_stock_news(selected_stock)
                if not news_df.empty:
                    for _, row in news_df.iterrows():
                        st.markdown(f"""
                        <div class="news-item">
                            <h4>{row['Title']}</h4>
                            <p>{row['Date']}</p>
                            <a href="{row['Link']}" target="_blank">Read More</a>
                        </div>
                        <hr>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recent news available")
        else:
            # Show specific error messages based on the error type
            if stock_info == "RATE_LIMITED":
                st.warning("🚫 **Yahoo Finance Rate Limited - Using Demo Mode**")
                st.info("""
                **Yahoo Finance is currently limiting requests, but don't worry!**
                
                I'll show you the dashboard with realistic sample data so you can explore all features:
                - Interactive price charts with technical indicators
                - Company metrics and financial ratios  
                - Complete dashboard functionality
                
                **To get real data:** Wait 10-15 minutes and try again, or use the app during off-peak hours.
                """)
                
                # Load sample data instead
                st.markdown("---")
                st.markdown("### 📊 Demo Mode - Sample Data Analysis")
                
                with st.spinner('Loading sample data...'):
                    sample_hist, sample_info = get_sample_stock_data(selected_stock, time_period)
                    
                if sample_hist is not None and sample_info is not None:
                    # Use the same analysis logic but with sample data
                    df = calculate_metrics(sample_hist)
                    
                    # Create tabs for different sections
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "📊 Price & Technical Analysis",
                        "🏢 Company Profile", 
                        "💰 Financial Metrics",
                        "📰 News"
                    ])
                    
                    with tab1:
                        st.info("📝 **Note:** This chart shows sample data due to Yahoo Finance rate limiting")
                        
                        # Technical Analysis Chart
                        st.plotly_chart(create_price_chart(df, selected_stock), use_container_width=True)
                        
                        # Summary metrics in a single row
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.markdown(f"""
                            <div class="stock-metric">
                                Current Price
                                <br/>
                                <span class="indicator-up">₹{format_number(sample_info.get('currentPrice', 0))}</span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            change = sample_info.get('regularMarketChangePercent', 0)
                            indicator_class = "indicator-up" if change >= 0 else "indicator-down"
                            st.markdown(f"""
                            <div class="stock-metric">
                                24h Change
                                <br/>
                                <span class="{indicator_class}">{change:.2f}%</span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col3:
                            st.markdown(f"""
                            <div class="stock-metric">
                                52 Week High
                                <br/>
                                <span>₹{format_number(sample_info.get('fiftyTwoWeekHigh', 0))}</span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col4:
                            st.markdown(f"""
                            <div class="stock-metric">
                                52 Week Low
                                <br/>
                                <span>₹{format_number(sample_info.get('fiftyTwoWeekLow', 0))}</span>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    with tab2:
                        st.info("📝 **Note:** This shows sample company data due to Yahoo Finance rate limiting")
                        
                        # Company Overview
                        st.subheader("Company Overview")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown("### Basic Information")
                            st.markdown(f"""
                            - **Company**: {sample_info.get('longName', 'Sample Company')}
                            - **Sector**: {sample_info.get('sector', 'Technology')}
                            - **Industry**: {sample_info.get('industry', 'Software')}
                            - **Employees**: {format_number(sample_info.get('fullTimeEmployees', 100000))}
                            """)
                        
                        with col2:
                            st.markdown("### Trading Information")
                            st.markdown(f"""
                            - **Exchange**: {sample_info.get('exchange', 'NSE')}
                            - **Currency**: {sample_info.get('currency', 'INR')}
                            - **Market Cap**: ₹{format_number(sample_info.get('marketCap', 0))}
                            """)
                        
                        with col3:
                            st.markdown("### Sample Metrics")
                            st.markdown(f"""
                            - **P/E Ratio**: {sample_info.get('trailingPE', 'N/A')}
                            - **Beta**: {sample_info.get('beta', 'N/A')}
                            - **Dividend Yield**: {sample_info.get('dividendYield', 0)*100:.2f}%
                            """)
                    
                    with tab3:
                        st.info("📝 **Note:** These are sample financial metrics due to Yahoo Finance rate limiting")
                        
                        # Financial Metrics using sample data
                        financial_metrics = get_financial_metrics(sample_info)
                        
                        # Valuation Metrics
                        st.subheader("Valuation Metrics")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Market Cap", financial_metrics['Market Cap'])
                            st.metric("P/E Ratio", financial_metrics['P/E Ratio'])
                            st.metric("EPS (TTM)", financial_metrics['EPS (TTM)'])
                        
                        with col2:
                            st.metric("Revenue (TTM)", financial_metrics['Revenue (TTM)'])
                            st.metric("Profit Margin", financial_metrics['Profit Margin'])
                            st.metric("Operating Margin", financial_metrics['Operating Margin'])
                        
                        with col3:
                            st.metric("ROE", financial_metrics['ROE'])
                            st.metric("Beta", financial_metrics['Beta'])
                            st.metric("Dividend Yield", financial_metrics['Dividend Yield'])
                    
                    with tab4:
                        st.info("📝 **Note:** News requires real-time data. Try again when Yahoo Finance is available.")
                        st.markdown("""
                        ### Sample News Headlines
                        - **Company Q3 Results:** Strong performance across key metrics
                        - **Market Update:** Sector outlook remains positive
                        - **Analyst Rating:** Upgraded to 'Buy' with revised price target
                        """)
                
                return  # Exit early since we've shown the demo
                
            elif stock_info == "NO_DATA":
                st.error(f"📊 **No Data Available**")
                st.warning(f"""
                The stock symbol **{selected_stock}** appears to be invalid or delisted.
                
                **Please try:**
                - Selecting a different stock from the dropdown
                - Checking if the symbol is correct
                """)
                
            elif stock_info == "INCOMPLETE_INFO":
                st.error("⚠️ **Incomplete Stock Information**")
                st.warning("""
                The stock data was partially loaded but missing key information.
                
                **Please try:**
                - Refreshing the page
                - Trying again in a few minutes
                - Selecting a different stock
                """)
                
            elif stock_info == "MAX_RETRIES_EXCEEDED":
                st.error("🔄 **Maximum Retries Exceeded**")
                st.warning("""
                We tried multiple times but couldn't load the stock data.
                
                **This usually means:**
                - Yahoo Finance is experiencing issues
                - Your internet connection might be unstable
                - The specific stock data is temporarily unavailable
                
                **Please try:**
                - Waiting 10-15 minutes and trying again
                - Selecting a different stock
                - Refreshing the browser page
                """)
                
            elif str(stock_info).startswith("ERROR:"):
                error_detail = str(stock_info).replace("ERROR: ", "")
                st.error("❌ **Technical Error Occurred**")
                st.warning(f"""
                **Error Details:** {error_detail}
                
                **Please try:**
                - Refreshing the page
                - Trying again in a few minutes
                - Contact support if the problem persists
                """)
                
            else:
                st.error('❌ **Error Loading Stock Data**')
                st.warning("""
                **General troubleshooting:**
                1. Wait a few minutes and try again
                2. Select a different stock
                3. Refresh the browser page
                4. Check your internet connection
                """)
            
            # Suggest alternative stocks
            st.markdown("### 🔄 Try These Popular Stocks Instead:")
            suggested_stocks = ['TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS', 'WIPRO.NS']
            cols = st.columns(len(suggested_stocks))
            for i, stock in enumerate(suggested_stocks):
                if stock != selected_stock:  # Don't suggest the same stock
                    with cols[i]:
                        if st.button(f"📈 {stock.replace('.NS', '')}", key=f"suggest_{stock}"):
                            st.session_state.selected_stock = stock
                            st.session_state.current_page = 'analysis'
                            st.rerun()

# Sidebar
st.sidebar.title('Indian Stock Analysis Dashboard')

# Handle navigation
if st.session_state.current_page == 'analysis':
    if st.sidebar.button('← Back to Home'):
        st.session_state.current_page = 'home'
        st.rerun()

    show_analysis(st.session_state.selected_stock, st.session_state.time_period)
else:
    # Home page
    selected_stock = st.sidebar.selectbox(
        'Select Indian Stock',
        default_stocks,
        format_func=lambda x: x.replace('.NS', '')  # Remove .NS suffix in display
    )

    # Enhanced time period selection
    time_selection = st.sidebar.radio(
        "Select Time Range Type",
        ["Predefined Periods", "Custom Range"]
    )

    if time_selection == "Predefined Periods":
        time_period = st.sidebar.selectbox(
            'Select Time Period',
            ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'max'],
            format_func=lambda x: {
                '1d': 'Last 24 Hours',
                '5d': 'Last 5 Days',
                '1mo': 'Last Month',
                '3mo': 'Last 3 Months',
                '6mo': 'Last 6 Months',
                '1y': 'Last Year',
                '2y': 'Last 2 Years',
                '5y': 'Last 5 Years',
                'max': 'Maximum Available'
            }[x]
        )
    else:
        time_period = 'custom'
        st.sidebar.markdown("### Select Custom Date Range")

        # Add minimum date validation
        min_date = datetime(2000, 1, 1)  # Stock data typically starts from 2000
        max_date = datetime.now()

        # Custom date range selectors with better formatting
        col1, col2 = st.sidebar.columns(2)
        with col1:
            st.session_state.custom_start_date = st.date_input(
                "From Date",
                value=st.session_state.custom_start_date,
                min_value=min_date,
                max_value=max_date,
                help="Select start date"
            )
        with col2:
            st.session_state.custom_end_date = st.date_input(
                "To Date",
                value=st.session_state.custom_end_date,
                min_value=st.session_state.custom_start_date,
                max_value=max_date,
                help="Select end date"
            )

    if st.sidebar.button('Analyze Stock', type='primary'):
        st.session_state.selected_stock = selected_stock
        st.session_state.time_period = time_period
        st.session_state.current_page = 'analysis'
        st.rerun()

    # Welcome message on home page
    st.title("Welcome to Indian Stock Analysis Dashboard")
    st.markdown("""
    ### How to use:
    1. Select an Indian stock from the sidebar
    2. Choose between predefined time periods or set a custom date range
    3. Click 'Analyze Stock' to see detailed analysis

    ### Available Features:
    - **Real-time Price Data**: Track current market prices and daily changes
    - **Technical Analysis**: View price trends and key indicators
    - **Company Profile**: Get detailed company information and ESG scores
    - **Financial Metrics**: Analyze key financial ratios and performance metrics
    - **Latest News**: Stay updated with company-specific news
    """)

    # Display available stocks in a grid
    st.subheader("Available Stocks")
    cols = st.columns(4)
    for i, stock in enumerate(default_stocks):
        company_name = stock.replace('.NS', '')
        cols[i % 4].markdown(f"• {company_name}")

# Footer
st.markdown("""
<div style='text-align: center; color: #666666; padding: 20px;'>
    Data provided by Yahoo Finance | Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST
</div>
""", unsafe_allow_html=True)