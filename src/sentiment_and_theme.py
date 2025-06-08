import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import re
import os

# ----------------------
# Setup
# ----------------------

# Load models
nlp = spacy.load("en_core_web_sm")
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Read all review data
df = pd.read_csv("data/cleaned_reviews.csv")

# Create output directory
os.makedirs("bank_sentiment_outputs", exist_ok=True)

# ----------------------
# Theme Keywords (Rule-based)
# ----------------------

theme_map = {
    "Account Access Issues": ["login", "password", "access", "reset", "locked", "credentials"],
    "Transaction Performance": ["transfer", "delay", "slow", "transaction", "failed"],
    "User Interface": ["interface", "layout", "design", "intuitive", "navigation"],
    "Customer Support": ["support", "agent", "response", "help", "chat"],
    "Feature Requests": ["feature", "add", "option", "missing", "setting"]
}

def assign_themes(text):
    matched_themes = []
    for theme, keywords in theme_map.items():
        if any(kw in text for kw in keywords):
            matched_themes.append(theme)
    return ", ".join(matched_themes) if matched_themes else "Other"

# ----------------------
# Preprocessing function
# ----------------------

def preprocess(text):
    text = re.sub(r"\s+", " ", text)
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# ----------------------
# Process Each Bank Separately
# ----------------------

banks = df["bank"].unique()

for bank in banks:
    print(f"\n🔍 Processing bank: {bank}")

    # Filter reviews for this bank
    bank_df = df[df["bank"] == bank].copy()

    # Add review ID
    bank_df["review_id"] = bank_df.index + 1

    # Clean text
    bank_df["cleaned_review"] = bank_df["review"].astype(str).apply(preprocess)

    # Sentiment
    sentiment_results = sentiment_pipeline(bank_df["review"].tolist(), truncation=True)
    bank_df["sentiment_label"] = [res["label"] for res in sentiment_results]
    bank_df["sentiment_score"] = [
        res["score"] if res["label"] == "POSITIVE" else -res["score"] for res in sentiment_results
    ]

    # TF-IDF (optional: view keywords per bank)
    vectorizer = TfidfVectorizer(max_features=50, ngram_range=(1, 2))
    vectorizer.fit(bank_df["cleaned_review"])
    top_keywords = vectorizer.get_feature_names_out()
    print(f"   ➤ Top keywords: {top_keywords[:10]}")

    # Thematic clustering
    bank_df["identified_themes"] = bank_df["cleaned_review"].apply(assign_themes)

    # Save results
    output_file = f"bank_sentiment_outputs/{bank.lower().replace(' ', '_')}_sentiment_theme_results.csv"
    bank_df[["review_id", "review", "sentiment_label", "sentiment_score", "identified_themes"]].to_csv(output_file, index=False)
    print(f"   ✅ Output saved to: {output_file}")
