# Customer-Experience-Analytics-for-Fintech-Apps

A starter repo to get everyone up and running with Python, Git, and GitHub Actions CI so you can focus on the challenge!

##  Quickstart

1. ## Fork and  clone

   ```bash
   git clone https://github.com/YeabsiraNigusse/Customer-Experience-Analytics-for-Fintech-Apps
   cd Predicting-Price-Moves-with-News-Sentiment
   ```

2. ## Create and activate virtual environment

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate      # macOS/Linux
    # .venv\Scripts\activate       # Windows PowerShell
    ```

3. ## Install dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. ## Branching and Workflow

- Branch off main for any work:
    ```bash
    git add .
    git commit -m "feat: describe your change"
    ```
5. ## Push and open a PR against main

    ```bash
    git push -u origin feature/your-feature
    ```

6. ## Project Structure Overview

- This repository contains all source code, documentation, and resources for the **Customer Experience Analytics for Fintech Apps** project.

        CUSTOMER-EXPERIENCE-ANALYTICS-FOR-FINTECH-APPS/
        ├── .github/ # GitHub Actions workflows (CI/CD automation)
        ├── .pytest_cache/ # Pytest cache files (auto-generated)
        ├── .venv/ # Virtual environment (Python dependencies)
        ├── .vscode/ # VSCode settings
        ├── src/ # Main source code and scripts
            │ ├── init.py # Marks this directory as a Python package
            │ ├── all_sentiment_analisys.py # Combines all banks' sentiment results
            │ ├── db_connection.py # Handles Oracle database connection setup
            │ ├── insert_reviews.py # Inserts cleaned reviews into Oracle database
            │ ├── insights_and_recommendation.md # Markdown file with generated insights
            │ ├── play_store_scraper.py # Scrapes app reviews from Google Play Store
            │ ├── preprocessor.py # Cleans and normalizes raw review data
            │ ├── sentiment_analisys.py # Sentiment scoring logic
            │ ├── sentiment_and_theme.py # Theme extraction and sentiment labeling
            │ ├── setup_database.py # Creates tables and schema in Oracle database
            │ ├── task_1.md # Task 1 summary: GitHub and CI/CD setup
            │ ├── task_2.md # Task 2 summary: Scraping and preprocessing
            │ └── README.md # README specific to src/ directory
        ├── tests/ # Unit tests for Python modules
        ├── LICENSE # License file for the project
        ├── README.md # Main project description and documentation
        ├── requirements.txt # Python dependencies
        ├── scraper.log # Logging output from scraping process
        ├── sentiment_distribution_by_bank.png # Visualization of sentiment breakdown


---

## 🔧 Description of Key Components

### `src/`
Core codebase including:
- **Scraping**: `play_store_scraper.py`
- **Preprocessing**: `preprocessor.py`
- **Sentiment analysis**: `sentiment_analisys.py`
- **Theme extraction**: `sentiment_and_theme.py`
- **Database operations**: `db_connection.py`, `setup_database.py`, `insert_reviews.py`
- **Results and insights**: `all_sentiment_analisys.py`, `insights_and_recommendation.md`

### `tests/`
Unit test suite for validating individual modules and functions.

### `.github/`
CI/CD workflows using GitHub Actions to automate testing and environment setup.

### `requirements.txt`
Lists all Python dependencies for setting up the environment.

### `scraper.log`
Stores log output during scraping for traceability and debugging.

### `sentiment_distribution_by_bank.png`
Graph showing sentiment distribution for each bank.
