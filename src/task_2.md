#  Task 2: Sentiment and Thematic Analysis

This module performs sentiment classification and thematic extraction from fintech app reviews to help identify what users like and dislike about different banks' mobile apps.

---

##  Objective

To:
- Quantify customer sentiment in reviews.
- Identify recurring **themes** (e.g., complaints, praise, feature mentions).
- Group results by bank for comparison and actionable insights.

---

## Input

- **File:** `cleaned_reviews.csv`
- **Columns Expected:**
  - `review_id`
  - `review`
  - `rating`
  - `date`
  - `bank`
  - `source`

---

##  Output

CSV files saved per bank in `bank_sentiment_outputs/`, each named:

Each file contains:
| review_id | review_text | sentiment_label | sentiment_score | identified_theme(s) | top_keywords |
|-----------|-------------|-----------------|------------------|----------------------|---------------|

---

##  Steps Followed

### 🔹 1. **Sentiment Analysis**

####  Model:
- `distilbert-base-uncased-finetuned-sst-2-english` from HuggingFace Transformers.

####  Process:
- Run sentiment classification for each review.
- Output:
  - `sentiment_label`: Positive / Negative
  - `sentiment_score`: Confidence (0–1)

####  Libraries:
- `transformers`, `torch`

---

### 🔹 2. **Thematic Analysis**

####  Goal:
Group recurring concepts into 3–5 **themes** per bank.

####  Process:
1. **Preprocessing with spaCy**
   - Tokenize, remove stopwords, and lemmatize.

2. **Keyword Extraction with TF-IDF**
   - Extract top unigrams, bigrams, and trigrams.
   - Score them based on relevance across reviews.

3. **Manual Grouping of Keywords**
   - Themes are manually defined by analyzing keyword clusters.
   - Typical themes include:
     -  Account Access Issues
     -  Transaction Problems
     -  UI/UX Experience
     -  Customer Support
     -  Feature Requests


