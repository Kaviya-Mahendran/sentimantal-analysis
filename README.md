
**Charity Sentiment Analysis**


Project Overview

This project analyzes the sentiment of charity categories to understand the general tone of charity descriptions. The sentiment can help identify whether a charity’s focus area or mission is described in positive, neutral, or negative language.

The project demonstrates skills in:

Data cleaning and preprocessing with pandas

Sentiment analysis using TextBlob

Visualization with matplotlib

Producing clean, shareable outputs (CSV, charts)

This project is designed as a mini-project for portfolios, showcasing data analysis and NLP capabilities.

Dataset

Source: Kaggle’s publicly available datasets on US charities

Example Dataset: nevada.csv

Columns:

Name, EIN, Category, Telephone, Address, City, State, Website, Facebook, Twitter, Income, Assests


Note: The analysis uses the Category column as descriptive text for sentiment evaluation.

Project Steps
1. Load Dataset

The CSV is loaded using pandas. Missing or empty values are handled.

import pandas as pd
df = pd.read_csv("nevada.csv")

2. Prepare Text

The Category column is converted to lowercase and cleaned for text analysis.

df['text'] = df['Category'].fillna("").str.lower()

3. Sentiment Analysis

Each category is analyzed using TextBlob. The polarity score determines the sentiment:

Polarity > 0 → Positive

Polarity < 0 → Negative

Polarity = 0 → Neutral

from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "positive"
    elif blob.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

df['sentiment'] = df['text'].apply(get_sentiment)

4. Save Results

The sentiment results are saved to a new CSV:

df.to_csv("nevada_charities_sentiment.csv", index=False)

5. Visualization

A bar chart shows the distribution of sentiment across all charities.

import matplotlib.pyplot as plt

sentiment_counts = df['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green','red','gray'])
plt.title("Sentiment of Nevada Charity Categories")
plt.xlabel("Sentiment")
plt.ylabel("Number of Charities")
plt.show()

Results

The CSV nevada_charities_sentiment.csv contains:

Name | EIN | Category | ... | text | sentiment


The bar chart shows how many charities fall into positive, neutral, or negative sentiment.

Insights:

Identify which categories are described positively vs neutrally.

Useful for understanding charity focus and communication style.

Dependencies

Install all required packages:

pip install pandas textblob matplotlib
python -m textblob.download_corpora


Python 3.x

pandas: data handling

TextBlob: sentiment analysis

matplotlib: visualization

How to Run

Clone the repository.

Place nevada.csv in the same folder as main.py.

Run the script:

python main.py


Outputs:

nevada_charities_sentiment.csv → sentiment results

Bar chart → sentiment distribution

Extensions / Future Work

Combine multiple state datasets (e.g., Nevada + Pennsylvania) for larger analysis.

Use charity mission statements or social media posts for more accurate sentiment analysis.

Apply advanced NLP techniques (VADER, spaCy) for better sentiment scoring.

Why Kaggle Dataset Was Used

The original goal was to scrape live websites for charity descriptions.

Many charity websites have restrictions (login, CAPTCHAs) and scraping could violate terms of service.

Using Kaggle datasets provides GDPR-friendly, publicly available data.

It allows focus on data analysis and sentiment modeling rather than dealing with scraping issues.
