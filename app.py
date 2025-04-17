import streamlit as st
import pandas as pd
from helper import parse_chat, get_most_active_days, get_hourly_activity
from visualization import plot_active_days, plot_hourly_activity, plot_emoji_usage
from sentiment import get_sentiment_distribution

# ✅ Streamlit UI
st.title("📊 WhatsApp Chat Analyzer")

# ✅ Upload Chat File
uploaded_file = st.file_uploader("Upload a WhatsApp Chat File (.txt)", type=["txt"])

if uploaded_file:
    df = parse_chat(uploaded_file)

    # ✅ Debugging - Show Data
    st.write("### Debugging DataFrame")
    st.write(df.head())  # Show first 5 rows
    st.write(f"Total messages: {len(df)}")

    if not df.empty:
        # ✅ Show Summary Statistics
        st.write("### Chat Summary")
        st.write(f"📅 Date Range: {df['Date'].min()} ➝ {df['Date'].max()}")
        st.write(f"💬 Total Messages: {len(df)}")

        # ✅ Active Days Visualization
        st.subheader("📅 Most Active Days")
        st.pyplot(plot_active_days(df))

        # ✅ Hourly Activity Visualization
        st.subheader("⏰ Hourly Activity")
        st.pyplot(plot_hourly_activity(df))

        # ✅ Emoji Usage Visualization
        st.subheader("😀 Most Used Emojis")
        st.pyplot(plot_emoji_usage(df))

        # ✅ Sentiment Analysis
        st.subheader("😊 Sentiment Analysis")
        sentiment_fig = get_sentiment_distribution(df)
        if sentiment_fig:
            st.pyplot(sentiment_fig)
        else:
            st.write("No sentiment data available.")

    else:
        st.error("❌ No messages found. Please check the file format.")
