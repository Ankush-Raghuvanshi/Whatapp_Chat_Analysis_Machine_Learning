from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_sentiment(message):
    """Analyzes the sentiment of a message using TextBlob."""
    analysis = TextBlob(message)
    return analysis.sentiment.polarity  # -1 (negative) to +1 (positive)

def get_sentiment_distribution(df):
    """Creates a pie chart for sentiment analysis."""
    if df.empty:
        print("❌ No messages for sentiment analysis.")
        return None

    df["Sentiment"] = df["Message"].apply(analyze_sentiment)

    sentiment_counts = df["Sentiment"].apply(lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral").value_counts()

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=["green", "red", "gray"])
    ax.set_title("Sentiment Analysis")
    return fig
