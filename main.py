import streamlit as st
import pandas as pd
from utils import get_stock_data, calculate_metrics, create_price_chart, format_number, get_stock_news

# Page configuration
st.set_page_config(
    page_title="Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Default Indian and US stocks
default_stocks = [
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS',  # Indian stocks
    'TATAMOTORS.NS', 'WIPRO.NS', 'ITC.NS', 'SUNPHARMA.NS', 'LT.NS',     # More Indian stocks
    'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META'  # US stocks
]

# Initialize session state variables if they don't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_stock' not in st.session_state:
    st.session_state.selected_stock = None
if 'time_period' not in st.session_state:
    st.session_state.time_period = '1y'

def show_analysis(selected_stock, time_period):
    """Show the analysis page content"""
    st.title(f"📈 {selected_stock} Analysis")

    # Load data
    with st.spinner('Loading stock data...'):
        hist_data, stock_info = get_stock_data(selected_stock, time_period)

        if hist_data is not None and stock_info is not None:
            # Calculate metrics
            df = calculate_metrics(hist_data)

            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(f"""
                <div class="stock-metric">
                    Current Price
                    <br/>
                    <span class="indicator-up">${format_number(stock_info.get('currentPrice', 0))}</span>
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
                    Market Cap
                    <br/>
                    <span>${format_number(stock_info.get('marketCap', 0))}</span>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="stock-metric">
                    Volume
                    <br/>
                    <span>{format_number(stock_info.get('volume', 0))}</span>
                </div>
                """, unsafe_allow_html=True)

            # Price chart
            st.plotly_chart(create_price_chart(df, selected_stock), use_container_width=True)

            # Additional metrics and news in two columns
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("### Key Statistics")
                metrics_df = pd.DataFrame({
                    'Metric': ['P/E Ratio', 'EPS', '52 Week High', '52 Week Low', 'Beta'],
                    'Value': [
                        format_number(stock_info.get('trailingPE', 0)),
                        format_number(stock_info.get('trailingEps', 0)),
                        format_number(stock_info.get('fiftyTwoWeekHigh', 0)),
                        format_number(stock_info.get('fiftyTwoWeekLow', 0)),
                        format_number(stock_info.get('beta', 0))
                    ]
                })
                st.dataframe(metrics_df, use_container_width=True)

            with col2:
                st.markdown("### Latest News")
                news_df = get_stock_news(selected_stock)
                if not news_df.empty:
                    for _, row in news_df.iterrows():
                        st.markdown(f"""
                        <div class="news-item">
                            <a href="{row['Link']}" target="_blank">{row['Title']}</a>
                            <br/>
                            <small>{row['Date']}</small>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recent news available")
        else:
            st.error('Error loading stock data. Please try again later.')

# Sidebar
st.sidebar.title('Stock Analysis Dashboard')

# Handle navigation
if st.session_state.current_page == 'analysis':
    if st.sidebar.button('← Back to Home'):
        st.session_state.current_page = 'home'
        st.rerun()

    show_analysis(st.session_state.selected_stock, st.session_state.time_period)
else:
    # Home page
    selected_stock = st.sidebar.selectbox('Select Stock', default_stocks)
    time_period = st.sidebar.select_slider(
        'Select Time Period',
        options=['1mo', '3mo', '6mo', '1y', '2y', '5y'],
        value='1y'
    )

    if st.sidebar.button('Analyze Stock'):
        st.session_state.selected_stock = selected_stock
        st.session_state.time_period = time_period
        st.session_state.current_page = 'analysis'
        st.rerun()

    # Welcome message on home page
    st.title("Welcome to Stock Analysis Dashboard")
    st.markdown("""
    ### How to use:
    1. Select a stock from the sidebar (includes both Indian and US stocks)
    2. Choose your preferred time period
    3. Click 'Analyze Stock' to see detailed analysis

    ### Available Stocks:
    - **Indian Markets**: RELIANCE, TCS, HDFC Bank, and more
    - **US Markets**: Apple, Google, Microsoft, and more
    """)

# Footer
st.markdown("""
<div style='text-align: center; color: #666666; padding: 20px;'>
    Data provided by Yahoo Finance | Updated daily
</div>
""", unsafe_allow_html=True)