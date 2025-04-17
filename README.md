WhatsApp_Chat_Analysis_Machine_Learning

🧾 1. Introduction

WhatsApp Chat Analysis is a data-driven project that extracts and visualizes insights from WhatsApp conversations. By analyzing chat history, the project uncovers interesting patterns such as:

Most active participants

Peak chatting hours

Emoji usage

Sentiment trends

The project helps users explore their chat data interactively using Python, Pandas, and Streamlit.

🎯 Project Aims:

Analyze personal or group conversations

Identify active users and messaging trends

Perform sentiment analysis to gauge emotional tone

Visualize chat activity through interactive graphs and charts

🎯 Project Objectives

Extract and structure WhatsApp chat data

Analyze message frequency patterns (daily, weekly, hourly)

Identify the most active participants in group chats

Detect commonly used words and emojis

Perform sentiment analysis (positive, negative, neutral)

Build an interactive dashboard using Streamlit

⚙️ Functionalities:

📥 Chat Parsing & Data Extraction

Reads exported WhatsApp .txt files

Uses Regex to extract timestamps, senders, and messages

Converts data into a structured Pandas DataFrame

📈 Message Frequency Analysis:

Tracks the most active days and hours

Identifies top contributors in group chats

Analyzes message volume over time

😊 Emoji Usage Statistics:

Extracts and visualizes emoji usage trends

Displays most frequently used emojis

☁️ Word Cloud & Common Words:

Highlights most used words (excluding stopwords)

Generates word cloud visualizations

💬 Sentiment Analysis:

Uses NLP (NLTK) for sentiment classification

Categorizes messages as Positive, Negative, or Neutral

Plots sentiment over time

📊 Interactive Data Visualization:

Streamlit-based dashboard

Includes interactive bar charts, line graphs, pie charts

Allows users to filter and explore insights dynamically

🛠️ Technologies Used
Languages & Libraries:

Python

Pandas

Regex (re)

Matplotlib & Seaborn

Emoji & WordCloud

NLTK (Natural Language Toolkit)

Streamlit

🔄 How It Works – Step-by-Step
1️⃣ Upload WhatsApp Chat File
Export chat from WhatsApp (.txt format)

Upload via Streamlit web app

2️⃣ Data Preprocessing
Parse chat with Regex

Convert to structured format: Date, Time, User, Message

3️⃣ Data Analysis & Visualization
Message trends (daily/hourly)

Top contributors

Emoji/word analysis

Sentiment classification

4️⃣ Interactive Dashboard
Filter and explore insights

Visual trends via charts and graphs

💼 Use Cases & Applications
👥 Personal Chat Analysis: Find your most active contacts and hours

🧑‍🤝‍🧑 Group Chat Insights: Identify talkative members and trends

📉 Sentiment Tracking: Useful for customer support and emotional tone analysis

🏢 Business/Research: Analyze customer conversations or topic trends in chats

🌟 Key Features
✅ Chat Parsing – Extract structured info from raw chat logs

📊 Message Frequency Analysis – Track active users and peak times

😊 Emoji Stats – View your most-used emojis

💬 Sentiment Analysis – Understand the tone of conversations

🧠 Interactive Dashboard – Explore all insights in a visual, user-friendly format
