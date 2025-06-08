import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessor import clean_review_files

def test_clean_review_files(tmp_path):
    # Create mock CSV files
    file1 = tmp_path / "reviews_1.csv"
    file2 = tmp_path / "reviews_2.csv"

    data = {
        "review_text": [" Great App ", "Bad experience"],
        "rating": [5, 1],
        "date": ["2022-01-01", "2022/02/01"],
        "bank_name": ["Bank A", "Bank B"],
        "source": ["Google", "PlayStore"]
    }

    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data)

    df1.to_csv(file1, index=False)
    df2.to_csv(file2, index=False)

    output_file = tmp_path / "cleaned.csv"
    clean_review_files(input_pattern=str(tmp_path / "*.csv"), output_file=str(output_file))

    result_df = pd.read_csv(output_file)

    # Test that it cleaned and combined both files
    assert len(result_df) == 2
    assert result_df['review'].iloc[0] == "Great App"
    assert result_df['bank'].iloc[1] == "Bank B"
    assert result_df['date'].iloc[0] == "2022-01-01"
