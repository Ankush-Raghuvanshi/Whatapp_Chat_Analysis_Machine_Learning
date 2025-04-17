import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import emoji

def plot_active_days(df):
    """Creates a bar chart for most active days."""
    if df.empty:
        print("❌ DataFrame is empty! No data to plot.")
        return None  

    daily_counts = df["Date"].value_counts().reset_index()
    daily_counts.columns = ["Date", "Message Count"]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Date", y="Message Count", data=daily_counts, ax=ax, palette="viridis")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    return fig

def plot_hourly_activity(df):
    """Creates a bar chart for hourly activity."""
    if df.empty:
        print("❌ DataFrame is empty! No data to plot.")
        return None  

    hourly_counts = df["Hour"].value_counts().reset_index()
    hourly_counts.columns = ["Hour", "Message Count"]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Hour", y="Message Count", data=hourly_counts, ax=ax, palette="magma")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    return fig

def plot_emoji_usage(df):
    """Creates a bar chart for the most used emojis."""
    all_emojis = []

    for message in df["Message"].dropna():
        all_emojis.extend([char for char in message if char in emoji.EMOJI_DATA])

    emoji_counts = Counter(all_emojis).most_common(10)  # Top 10 most used emojis
    if not emoji_counts:
        print("❌ No emojis found.")
        return None  

    emojis, counts = zip(*emoji_counts)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=list(emojis), y=list(counts), ax=ax, palette="coolwarm")
    ax.set_ylabel("Count")
    ax.set_xlabel("Emoji")
    return fig
