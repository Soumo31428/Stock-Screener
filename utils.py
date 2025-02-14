import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import trafilatura
from datetime import datetime, timedelta

def get_stock_data(symbol, period='1y', start_date=None, end_date=None):
    """Fetch stock data using yfinance"""
    try:
        stock = yf.Ticker(symbol)
        if period == 'custom' and start_date and end_date:
            hist = stock.history(start=start_date, end=end_date)
        else:
            hist = stock.history(period=period)
        info = stock.info
        return hist, info
    except Exception as e:
        print(f"Error fetching stock data: {str(e)}")
        return None, None

def calculate_metrics(df):
    """Calculate technical indicators"""
    # Basic moving averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # RSI
    df['RSI'] = calculate_rsi(df['Close'])

    # MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

    # Bollinger Bands
    df['BB_middle'] = df['Close'].rolling(window=20).mean()
    df['BB_upper'] = df['BB_middle'] + 2 * df['Close'].rolling(window=20).std()
    df['BB_lower'] = df['BB_middle'] - 2 * df['Close'].rolling(window=20).std()

    return df

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def create_price_chart(df, symbol):
    """Create an interactive price chart with indicators"""
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.03, 
                        row_heights=[0.6, 0.2, 0.2])

    # Candlestick chart with Bollinger Bands
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='OHLC'
        ),
        row=1, col=1
    )

    # Add Bollinger Bands
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['BB_upper'],
            name='BB Upper',
            line=dict(color='rgba(250, 250, 250, 0.4)'),
            fill=None
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['BB_lower'],
            name='BB Lower',
            line=dict(color='rgba(250, 250, 250, 0.4)'),
            fill='tonexty',
            fillcolor='rgba(250, 250, 250, 0.1)'
        ),
        row=1, col=1
    )

    # Add SMAs
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['SMA_20'],
            name='SMA 20',
            line=dict(color='#00FF9D')
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['SMA_50'],
            name='SMA 50',
            line=dict(color='#FF4B4B')
        ),
        row=1, col=1
    )

    # Volume bars
    colors = ['#4BFF4B' if row['Close'] >= row['Open'] else '#FF4B4B' for index, row in df.iterrows()]
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df['Volume'],
            name='Volume',
            marker_color=colors
        ),
        row=2, col=1
    )

    # RSI
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['RSI'],
            name='RSI',
            line=dict(color='#00FF9D')
        ),
        row=3, col=1
    )

    # Add RSI levels
    fig.add_hline(y=70, line_color='#FF4B4B', line_width=1, line_dash='dash', row=3, col=1)
    fig.add_hline(y=30, line_color='#4BFF4B', line_width=1, line_dash='dash', row=3, col=1)

    # Update layout
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='#1E1E1E',
        plot_bgcolor='#2D2D2D',
        xaxis_rangeslider_visible=False,
        height=800,
        showlegend=True
    )

    # Update y-axes labels
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)
    fig.update_yaxes(title_text="RSI", row=3, col=1)

    return fig

def format_number(number):
    """Format large numbers with K, M, B suffixes"""
    try:
        if pd.isna(number) or number == 0:
            return "N/A"
        if number >= 1e9:
            return f"{number/1e9:.2f}B"
        elif number >= 1e6:
            return f"{number/1e6:.2f}M"
        elif number >= 1e3:
            return f"{number/1e3:.2f}K"
        return f"{number:.2f}"
    except:
        return "N/A"

def get_stock_news(symbol):
    """Get latest news for the stock"""
    try:
        company_symbol = symbol.replace('.NS', '')
        stock = yf.Ticker(symbol)
        news = stock.news

        news_data = []
        for item in news[:5]:  # Get latest 5 news items
            news_data.append({
                'Title': item['title'],
                'Date': datetime.fromtimestamp(item['providerPublishTime']).strftime('%Y-%m-%d'),
                'Link': item['link']
            })

        return pd.DataFrame(news_data)
    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        return pd.DataFrame(columns=['Title', 'Date', 'Link'])

def get_company_profile(info):
    """Format company profile information"""
    profile = {
        'Business Summary': info.get('longBusinessSummary', 'N/A'),
        'Sector': info.get('sector', 'N/A'),
        'Industry': info.get('industry', 'N/A'),
        'Website': info.get('website', 'N/A'),
        'Full Time Employees': format_number(info.get('fullTimeEmployees', 0)),
    }
    return profile

def get_financial_metrics(info):
    """Get key financial metrics"""
    metrics = {
        'Market Cap': format_number(info.get('marketCap', 0)),
        'P/E Ratio': format_number(info.get('trailingPE', 0)),
        'EPS (TTM)': format_number(info.get('trailingEps', 0)),
        'Beta': format_number(info.get('beta', 0)),
        'Dividend Yield': f"{format_number(info.get('dividendYield', 0) * 100)}%" if info.get('dividendYield') else 'N/A',
        'Revenue (TTM)': format_number(info.get('totalRevenue', 0)),
        'Profit Margin': f"{format_number(info.get('profitMargins', 0) * 100)}%",
        'Operating Margin': f"{format_number(info.get('operatingMargins', 0) * 100)}%",
        'ROE': f"{format_number(info.get('returnOnEquity', 0) * 100)}%",
        'ROA': f"{format_number(info.get('returnOnAssets', 0) * 100)}%",
        'Debt to Equity': format_number(info.get('debtToEquity', 0)),
        'Current Ratio': format_number(info.get('currentRatio', 0)),
    }
    return metrics