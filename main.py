import streamlit as st
import pandas as pd
from utils import get_stock_data, calculate_metrics, create_price_chart, format_number

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

# Sidebar
st.sidebar.title('Stock Analysis Dashboard')
default_stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META']
selected_stock = st.sidebar.selectbox('Select Stock', default_stocks)
time_period = st.sidebar.select_slider(
    'Select Time Period',
    options=['1mo', '3mo', '6mo', '1y', '2y', '5y'],
    value='1y'
)

# Main content
st.title(f"📈 {selected_stock} Stock Analysis")

# Load data
with st.spinner('Loading stock data...'):
    hist_data, stock_info = get_stock_data(selected_stock, time_period)
    
    if hist_data is not None and stock_info is not None:
        # Calculate metrics
        df = calculate_metrics(hist_data)
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="stock-metric">
                Current Price
                <br/>
                <span class="indicator-up">$""" + 
                format_number(stock_info.get('currentPrice', 0)) + 
                """</span>
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
            st.markdown("""
            <div class="stock-metric">
                Market Cap
                <br/>
                <span>$""" + 
                format_number(stock_info.get('marketCap', 0)) + 
                """</span>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown("""
            <div class="stock-metric">
                Volume
                <br/>
                <span>""" + 
                format_number(stock_info.get('volume', 0)) + 
                """</span>
            </div>
            """, unsafe_allow_html=True)

        # Price chart
        st.plotly_chart(create_price_chart(df, selected_stock), use_container_width=True)

        # Additional metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Key Statistics
            """)
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
            st.markdown("""
            ### Company Info
            """)
            st.write(stock_info.get('longBusinessSummary', 'No information available'))

    else:
        st.error('Error loading stock data. Please try again later.')

# Footer
st.markdown("""
<div style='text-align: center; color: #666666; padding: 20px;'>
    Data provided by Yahoo Finance | Updated daily
</div>
""", unsafe_allow_html=True)
