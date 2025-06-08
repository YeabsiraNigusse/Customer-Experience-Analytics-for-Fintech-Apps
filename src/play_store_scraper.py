import os
from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import schedule
import logging
import time



print("Starting script...")  # Always visible in terminal
logging.basicConfig(
    filename=os.path.abspath('scraper.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("🚀 Script started")

def scrape_play_store_reviews():
    APP_ID = 'com.boa.boaMobileBanking'
    logging.info("🔄 Fetching reviews...")

    try:
        results, _ = reviews(
            APP_ID,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=5000,
            filter_score_with=None
        )

        logging.info(f"📥 Retrieved {len(results)} reviews")

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'Abyssinia_Bank_{timestamp}.csv'

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
            writer.writeheader()

            for entry in results:
                writer.writerow({
                    'review_text': entry['content'],
                    'rating': entry['score'],
                    'date': entry['at'].strftime('%Y-%m-%d'),
                    'bank_name': 'Bank of Abyssinia',
                    'source': 'Google Play'
                })

        logging.info(f"✅ Saved {len(results)} reviews to {filename}")
    except Exception as e:
        logging.error(f"❌ Error occurred: {e}")

# Schedule and run once immediately for testing
scrape_play_store_reviews()  # <- force one run

# schedule.every(6).hours.do(scrape_play_store_reviews)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
