import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load each bank's data
boa_df = pd.read_csv("data/bank_sentiment_outputs/bank_of_abyssinia_sentiment_theme_results.csv")
boa_df["bank"] = "Bank of Abyssinia"

cbe_df = pd.read_csv("data/bank_sentiment_outputs/commercial_bank_of_ethiopia_sentiment_theme_results.csv")
cbe_df["bank"] = "Commercial Bank of Ethiopia"

dashen_df = pd.read_csv("data/bank_sentiment_outputs/dashen_bank_sentiment_theme_results.csv")
dashen_df["bank"] = "Dashen Bank"

# Combine all into one DataFrame
df_all = pd.concat([boa_df, cbe_df, dashen_df], ignore_index=True)

print(df_all.head())
print(df_all["bank"].value_counts())


plt.figure(figsize=(10, 6))
sns.countplot(data=df_all, x='bank', hue='sentiment_label')
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Review Count")
plt.legend(title="Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sentiment_distribution_by_bank.png")
plt.show()