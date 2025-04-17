import re
import pandas as pd

def parse_chat(uploaded_file):
    """Parses a WhatsApp chat file into a structured DataFrame."""
    raw_lines = uploaded_file.read().decode('utf-8', errors='ignore').split("\n")

    # ✅ Print first 10 lines for debugging
    print("\n🔍 Chat File First 10 Lines:")
    for line in raw_lines[:10]:
        print(line)

    # ✅ Define multiple regex patterns to handle different formats
    patterns = [
        r'(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} (AM|PM)) - (.*?): (.*)',  # Standard format
        r'\[(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2})\] (.*?): (.*)',  # Bracket format
        r'(\d{1,2}\.\d{1,2}\.\d{2,4}, \d{1,2}:\d{2} (AM|PM)) - (.*?): (.*)'  # European format
    ]

    messages = []
    for line in raw_lines:
        if "end-to-end encrypted" in line:  
            continue  # Skip encryption messages

        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                timestamp, _, user, message = match.groups()
                messages.append([timestamp, user, message])
                break  

    if not messages:
        print("❌ No messages found. Check file format.")
        return pd.DataFrame()

    # ✅ Convert parsed messages into a DataFrame
    df = pd.DataFrame(messages, columns=["Timestamp", "User", "Message"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df.dropna(subset=["Timestamp"], inplace=True)
    df["Date"] = df["Timestamp"].dt.date
    df["Hour"] = df["Timestamp"].dt.hour

    return df 


def get_most_active_days(df):
    """Returns the most active days based on message count."""
    return df["Date"].value_counts().head(10)


def get_hourly_activity(df):
    """Returns message distribution by hour."""
    return df["Hour"].value_counts().sort_index()


if __name__ == "__main__":
    # ✅ Test parsing function with a sample file (Run manually for debugging)
    with open(r"E:\whatsapp-chat-analyzer\WhatsApp Chat.txt", "r", encoding="utf-8") as f:
        df = parse_chat(f)
        print(df.head())
