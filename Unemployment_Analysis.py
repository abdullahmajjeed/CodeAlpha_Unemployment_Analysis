import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration (Full width layout)
st.set_page_config(page_title="Unemployment Analysis Dashboard", layout="wide")

# Custom Styling for modern look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .metric-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Banner
st.title("📊 2020 Lockdown: Unemployment Analysis Dashboard")
st.caption("This dashboard explores patterns within regional unemployment tracking metrics.")

# File Uploader component inside a card layout (Not in sidebar)
uploaded_file = st.file_uploader("📂 Drag and drop your 'Unemployment_in_India.csv' file here", type=["csv"])

if uploaded_file is not None:
    # 1. Data Ingestion & Sanitization Logic from Notebook
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')
    df['Region'] = df['Region'].str.strip()
    df['Area'] = df['Area'].str.strip()
    
    # 2. Modern Top Navigation Tabs (Naya Interface Grid)
    tab1, tab2, tab3 = st.tabs(["📌 Overview & KPIs", "📈 Timeline Trends", "🗺️ Regional & Sector Breakdown"])
    
    with tab1:
        st.subheader("Key Performance Indicators (KPIs)")
        
        # Using Streamlit's native metrics which support both Dark and Light themes perfectly
        col1, col2, col3 = st.columns(3)
    with col1:
            st.metric(
                label="Avg Unemployment Rate", 
                value=f"{df['Estimated Unemployment Rate (%)'].mean():.2f}%"
            )
    with col2:
            st.metric(
                label="Max Unemployment Recorded", 
                value=f"{df['Estimated Unemployment Rate (%)'].max():.2f}%"
            )
    with col3:
            st.metric(
                label="Avg Labour Participation", 
                value=f"{df['Estimated Labour Participation Rate (%)'].mean():.2f}%"
            )
            
    st.markdown("---")
    st.subheader("Sanitized Data Preview")
    st.dataframe(df.style.background_gradient(cmap='Blues'), use_container_width=True)


    with tab2:
        st.subheader("National Unemployment Rate Trendline Over Time")
        
        # Temporal Aggregation Logic from Notebook
        monthly_timeline = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
        
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.set_theme(style='ticks')
        ax.plot(monthly_timeline['Date'], monthly_timeline['Estimated Unemployment Rate (%)'], marker='o', color='crimson', linewidth=2)
        ax.set_xlabel('Timeline Frame')
        ax.set_ylabel('Mean Unemployment Rate (%)')
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
    with tab3:
        st.subheader("Sectors & Regions Comparative Analysis")
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.write("### Sector Distribution (Rural vs Urban)")
            fig2, ax2 = plt.subplots(figsize=(6, 5))
            sns.boxplot(data=df, x='Area', y='Estimated Unemployment Rate (%)', palette='Pastel1', ax=ax2)
            st.pyplot(fig2)
            
        with col_right:
            st.write("### Ranked Regional Unemployment Rates")
            regional_stats = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).reset_index()
            fig3, ax3 = plt.subplots(figsize=(6, 5))
            sns.barplot(data=regional_stats, x='Estimated Unemployment Rate (%)', y='Region', palette='viridis', ax=ax3)
            st.pyplot(fig3)

else:
    st.info("💡 Please upload your CSV file above to begin the dashboard analysis.")
