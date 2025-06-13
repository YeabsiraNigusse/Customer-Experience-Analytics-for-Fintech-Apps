import pandas as pd
from db_connection import get_connection

def insert_banks(bank_names):
    conn = get_connection()
    cursor = conn.cursor()
    for name in bank_names:
        try:
            cursor.execute("INSERT INTO banks (name) VALUES (:1)", (name,))
        except Exception:
            pass
    conn.commit()
    cursor.close()
    conn.close()

def get_bank_id(bank_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM banks WHERE name = :1", (bank_name,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return row[0]
    return None

def insert_reviews(df):
    conn = get_connection()
    cursor = conn.cursor()
    inserted = 0
    skipped = 0

    for _, row in df.iterrows():
        bank_name = row['bank']
        bank_id = get_bank_id(bank_name)
        if not bank_id:
            print(f"Skipping unknown bank: {bank_name}")
            skipped += 1
            continue
        try:
            cursor.execute("""
                INSERT INTO reviews (bank_id, review_text, sentiment, theme, review_date)
                VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
            """, (bank_id, row['review'], row.get('sentiment'), row.get('theme'), row['review_date']))
            inserted += 1
        except Exception as e:
            print(f"Error inserting review: {e}")
            skipped += 1

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted: {inserted} rows")
    print(f"Skipped: {skipped} rows")

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_reviews.csv')
    df['review_date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    unique_banks = df['bank'].unique().tolist()
    insert_banks(unique_banks)  # Insert all unique banks first
    insert_reviews(df)
