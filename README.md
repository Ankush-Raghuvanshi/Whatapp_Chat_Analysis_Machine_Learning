# Whatapp_Chat_Analysis_Machine_Learning
1. Introduction:
WhatsApp Chat Analysis is a data-driven project that extracts and visualizes insights
from WhatsApp conversations. By analyzing chat history, we can uncover interesting
patterns, such as the most active participants, peak chatting hours, emoji usage, and
sentiment trends. This project helps users explore their chat data interactively using
Python, Pandas, and Streamlit.
This project aims to:
 Analyze personal or group conversations
 Identify the most active users and message trends
 Perform sentiment analysis to gauge emotional tone
 Visualize chat activity through interactive graphs and charts.
Project Objectives
1. Extract and structure WhatsApp chat data
2. Analyze message frequency patterns (daily, weekly, and hourly trends)
3. Identify the most active participants in group chats
4. Detect the most commonly used words and emojis
5. Perform sentiment analysis on messages (positive, negative, neutral)
6. Build an interactive dashboard using Streamlit

Functionalities:
Chat Parsing &amp; Data Extraction
 Reads the exported WhatsApp chat file (.txt format)
 Uses Regular Expressions (Regex) to extract timestamps, senders, and messages
 Converts the extracted data into a structured Pandas DataFrame.

Message Frequency Analysis
 Finds the most active days and hours
 Identifies top contributors in a group chat
 Tracks message volume over time
Emoji Usage Statistics
 Extracts emojis used in messages
 Identifies the most frequently used emojis
 Creates visualizations of emoji trends
Word Cloud &amp; Common Words
 Identifies the most used words (excluding stop words like “the”, “is”, etc.)
 Generates a word cloud for visualization
Sentiment Analysis
 Uses Natural Language Processing (NLP) to analyze message sentiment
 Categorizes messages as positive, negative, or neutral
 Plots sentiment trends over time
Interactive Data Visualization
 Streamlit-based dashboard for exploring chat insights
 Interactive bar charts, line graphs, and pie charts
 Allows users to filter and explore data dynamically


Technologies Used
Programming Languages &amp; Libraries
 Python – Main programming language
 Pandas – Data processing and analysis
 Regular Expressions (re) – Extracting patterns from chat data
 Matplotlib &amp; Seaborn – Data visualization
 Emoji &amp; WordCloud – Emoji extraction and word frequency analysis
 NLTK (Natural Language Toolkit) – Sentiment analysis
 Streamlit – Interactive UI and dashboard.

How It Works – Step-by-Step
1️ Upload WhatsApp Chat File
 Export a chat from WhatsApp (.txt file)
 Upload the file in the Streamlit web app
2️ Data Preprocessing
 The script parses chat messages using regex
 Converts data into a structured format (Date, Time, User, Message)
3️ Data Analysis &amp; Visualization
 Message activity trends (daily, hourly)
 Top contributors in group chats
 Emoji and word frequency analysis
 Sentiment classification of messages
4️ Display Results in an Interactive Dashboard
 Users can filter, sort, and explore the chat insights
 Graphs and charts make it easy to understand trends visually


Use Cases &amp; Applications
�� Personal Chat Analysis
 Find out who texts the most in your personal chats
 Identify your most active hours and days
�� Group Chat Insights
 Discover the most talkative members of a group
 Track engagement trends over time
�� Sentiment Tracking
 Monitor positive or negative trends in conversations
 Useful for customer support chats to detect user sentiment
�� Business &amp; Research Applications
 Analyze customer conversations for sentiment and trends
 Extract key topics from group discussions

Key Features
 Chat Parsing: Extracts structured data (timestamps, senders, and messages) from raw
chat files.
 Message Frequency Analysis: Identifies the most active users and peak conversation
times.
 Emoji Usage Statistics: Displays the most frequently used emojis.
 Sentiment Analysis: Analyzes whether the conversation is positive, negative, or
neutral.
 Interactive Dashboard: Uses Streamlit to visualize the data with graphs and charts.

