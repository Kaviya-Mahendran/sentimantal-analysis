import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

# --- Step 1: Load the CSV ---
csv_file = "nevada.csv"
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"{csv_file} not found in project folder.")

df = pd.read_csv(csv_file)
print("Columns in CSV:", df.columns)
print(df.head())

# --- Step 2: Prepare text for sentiment analysis ---
# We'll use the 'Category' column for sentiment analysis
df['text'] = df['Category'].fillna("").str.lower()

# --- Step 3: Perform sentiment analysis ---
def get_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "positive"
    elif blob.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

df['sentiment'] = df['text'].apply(get_sentiment)

# --- Step 4: Save results to new CSV ---
output_csv = "nevada_charities_sentiment.csv"
df.to_csv(output_csv, index=False)
print(f"Sentiment results saved to '{output_csv}'")

# --- Step 5: Visualization ---
sentiment_counts = df['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Sentiment of Nevada Charity Categories")
plt.xlabel("Sentiment")
plt.ylabel("Number of Charities")
plt.tight_layout()
plt.show()
