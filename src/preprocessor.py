import pandas as pd
import glob
from datetime import datetime
import os

def clean_review_files(input_pattern="data/*_reviews_*.csv", output_file="data/cleaned_reviews.csv"):
    all_files = glob.glob(input_pattern)
    dataframes = []

    print(f"🔍 Found {len(all_files)} files matching pattern '{input_pattern}'")

    for file in all_files:
        try:
            df = pd.read_csv(file)
            print(f"📂 Processing file: {file} ({len(df)} rows)")

            # Rename columns
            df.rename(columns={
                'review_text': 'review',
                'bank_name': 'bank'
            }, inplace=True)

            # Normalize dates
            df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

            # Drop rows with missing critical fields
            df.dropna(subset=['review', 'rating', 'date', 'bank', 'source'], inplace=True)

            # Strip whitespace
            df['review'] = df['review'].astype(str).str.strip()
            df['bank'] = df['bank'].astype(str).str.strip()
            df['source'] = df['source'].astype(str).str.strip()

            if not df.empty:
                dataframes.append(df)
            else:
                print(f"⚠️ Skipped empty dataframe from file: {file}")

        except Exception as e:
            print(f" Error processing {file}: {e}")

    # Combine and save
    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df.drop_duplicates(subset=['review', 'date', 'bank'], inplace=True)
        combined_df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file} ({len(combined_df)} rows)")
    else:
        print("No valid data to save. Check your input files.")

# Run the cleaner
clean_review_files()
