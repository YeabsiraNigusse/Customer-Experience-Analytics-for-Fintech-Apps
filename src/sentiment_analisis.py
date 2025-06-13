import pandas as pd

df = pd.read_csv("data/bank_sentiment_outputs/bank_of_abyssinia_sentiment_theme_results.csv")
print(df.head())
print(df['sentiment_label'].value_counts())
print(df['identified_themes'].value_counts())


positive_reviews = df[df['sentiment_label'] == 'POSITIVE']
driver_counts = positive_reviews['identified_themes'].value_counts()
print("Positive Drivers:\n", driver_counts.head())


negative_reviews = df[df['sentiment_label'] == 'NEGATIVE']
pain_counts = negative_reviews['identified_themes'].value_counts()
print("Pain Points:\n", pain_counts.head())


df = pd.read_csv("data/bank_sentiment_outputs/commercial_bank_of_ethiopia_sentiment_theme_results.csv")
print(df.head())
print(df['sentiment_label'].value_counts())
print(df['identified_themes'].value_counts())


positive_reviews = df[df['sentiment_label'] == 'POSITIVE']
driver_counts = positive_reviews['identified_themes'].value_counts()
print("Positive Drivers:\n", driver_counts.head())


negative_reviews = df[df['sentiment_label'] == 'NEGATIVE']
pain_counts = negative_reviews['identified_themes'].value_counts()
print("Pain Points:\n", pain_counts.head())


df = pd.read_csv("data/bank_sentiment_outputs/dashen_bank_sentiment_theme_results.csv")
print(df.head())
print(df['sentiment_label'].value_counts())
print(df['identified_themes'].value_counts())


positive_reviews = df[df['sentiment_label'] == 'POSITIVE']
driver_counts = positive_reviews['identified_themes'].value_counts()
print("Positive Drivers:\n", driver_counts.head())


negative_reviews = df[df['sentiment_label'] == 'NEGATIVE']
pain_counts = negative_reviews['identified_themes'].value_counts()
print("Pain Points:\n", pain_counts.head())