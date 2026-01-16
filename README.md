**Charity Sentimental Analysis**

**A. Project Overview**

This project implements a practical NLP pipeline to analyse sentiment across charity categories and extract meaningful signals about how nonprofits present their focus areas. Instead of a one-off exploration, this repository is designed as an end-to-end workflow that turns textual descriptions into analytical insight — sentiment categories, structured outputs, and visual summaries that help compare and prioritise patterns.

This work illustrates real analytic reasoning, from data preparation → text processing → sentiment scoring → interpretation. It’s built for clarity, reproducibility, and extension into deeper NLP or behavioural analysis.

Although implementations vary across organisations, these principles apply broadly to most data analytics environments.

**B. System Architecture Diagram**

Below is a conceptual overview of how data flows through the project:

Raw Dataset (Charity descriptions CSV)
       ↓
Preprocessing (Text cleaning & normalization)
       ↓
Sentiment Analysis (TextBlob-based scoring)
       ↓
Structured Outputs (CSV with sentiment labels)
       ↓
Visualization & Interpretation (Charts + summaries)


Every stage is designed to be independent, testable, and reusable, so improvements in one phase don’t force rework everywhere else.

**C. Step-by-Step Workflow**
**Step 1: Load & Prepare Raw Data**

The project starts with a charity dataset (e.g., nevada.csv) loaded into a pandas DataFrame. The text column (such as charity category) is extracted and normalized (lowercasing, filling null values).

import pandas as pd

df = pd.read_csv("nevada.csv")
df['text'] = df['Category'].fillna("").str.lower()


This ensures text is consistent and clean before analysis.

**Step 2: Preprocess & Clean Text**

Text preprocessing removes noise so sentiment scoring isn’t skewed by capitals, punctuation, or missing values:

Lowercasing

Null handling

Simple cleaning functions

This gives the pipeline a stable foundation to measure sentiment meaningfully.

**Step 3: Sentiment Scoring**

Using TextBlob, each text item is assigned a sentiment polarity:

Positive if polarity > 0

Neutral if polarity == 0

Negative if polarity < 0

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


This step turns free text into structured sentiment labels ready for analysis.

**Step 4: Generate Structured Outputs**

The pipeline outputs a clean CSV (nevada_charities_sentiment.csv) that includes:

original fields

cleaned text

sentiment labels

This file can be loaded into dashboards, BI tools, or used for further NLP layering.

**Step 5: Visualize & Interpret Results**

The project includes a visualization of sentiment distribution:

import matplotlib.pyplot as plt

sentiment_counts = df['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green','gray','red'])
plt.title("Sentiment of Nevada Charity Categories")
plt.xlabel("Sentiment")
plt.ylabel("Number of Charities")
plt.show()


This visualization helps communicate patterns at a glance — e.g., which categories are described positively versus neutrally.

**D. Why This Matters**
Reducing Manual Work

This pipeline eliminates repeated manual cleaning and sentiment scoring that would otherwise be done with spreadsheets or ad-hoc scripts. Once run, it consistently produces the same structured dataset every time.

Supporting Nonprofit Decisions

Sentiment patterns in charity descriptions can guide operational decisions such as:

understanding how focus areas are framed

identifying outreach or branding gaps

comparing similarities across organisations

For resource-constrained teams, converting text into patterns frees analysts to focus on strategy rather than cleanup.

Innovation Beyond Occupation

This project demonstrates how a lightweight NLP pipeline can be used by organisations of any size to extract behavioural signals from text — without deep AI infrastructure. It shows how analytics can systematically augment intuition with data evidence, an approach valuable well beyond this specific dataset.

Although implementations vary across organisations, these principles apply broadly to most data analytics environments.

**E. Reflection & Learnings**

Working on this pipeline highlighted how real text analytics projects are shaped less by complexity and more by clarity of purpose.

Key takeaways include:

Preprocessing matters more than model choice: Small text normalization steps greatly improved sentiment quality.

Structured outputs make analytics possible: A clean sentiment CSV can be used by any analyst or stakeholder.

Interpretability accelerates adoption: Simple visual summaries turned abstract scores into actionable understanding.

This exercise also reinforced that analytics is more than code — it’s about designing workflows that deliver reliable, reusable data. When others can pick up the repo and understand it without hand-holding, that’s when technical work becomes a community asset.

For analysts reading this, start by asking:
“What story do I want data to serve?”
Build your pipelines to answer that question, not just produce outputs.

**How to Run**

Clone the repository

Place nevada.csv in the root folder

Install dependencies (e.g., pandas, textblob, matplotlib)

**Run:**

python main.py


**Review the generated nevada_charities_sentiment.csv and chart outputs
**
