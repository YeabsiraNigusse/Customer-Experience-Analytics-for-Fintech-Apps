import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.sentiment_and_theme import analyze_sentiment_and_theme

def test_analyze_sentiment_and_theme(tmp_path):
    # Create a fake cleaned review file
    test_file = tmp_path / "cleaned_reviews.csv"
    df = pd.DataFrame({
        "review": ["Good app", "Worst app ever", "Not bad", "Very buggy"],
        "rating": [5, 1, 3, 2],
        "date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"],
        "bank": ["Test Bank", "Test Bank", "Test Bank", "Test Bank"],
        "source": ["Google", "Google", "Google", "Google"]
    })
    df.to_csv(test_file, index=False)

    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Run the function
    analyze_sentiment_and_theme(str(test_file), str(output_dir))

    # Check if output file was created
    result_file = output_dir / "task2_test_bank_sentiment_theme_results.csv"
    assert result_file.exists()

    # Check contents
    result_df = pd.read_csv(result_file)
    assert "sentiment_label" in result_df.columns
    assert "theme_keywords" in result_df.columns
