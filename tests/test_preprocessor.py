import pandas as pd
from src.preprocessor import clean_review_files

def test_clean_review_files(tmp_path):
    # Create mock CSV files
    file1 = tmp_path / "reviews_1.csv"
    file2 = tmp_path / "reviews_2.csv"

    data1 = {
        "review_text": [" Great App ", "Bad experience"],
        "rating": [5, 1],
        "date": ["2022-01-01", "2022/02/01"],
        "bank_name": ["Bank A", "Bank B"],
        "source": ["Google", "PlayStore"]
    }

    data2 = {
        "review_text": [" Excellent ", "Terrible experience"],
        "rating": [5, 1],
        "date": ["2022-01-03", "2022/02/03"],
        "bank_name": ["Bank A", "Bank C"],
        "source": ["Google", "AppStore"]
    }

    pd.DataFrame(data1).to_csv(file1, index=False)
    pd.DataFrame(data2).to_csv(file2, index=False)

    output_file = tmp_path / "cleaned.csv"
    clean_review_files(input_pattern=str(tmp_path / "*.csv"), output_file=str(output_file))

    result_df = pd.read_csv(output_file)

    # ✅ Updated: Expect only 2 rows due to deduplication
    assert len(result_df) == 2

    # Optionally, verify actual contents
    expected_reviews = set(["Excellent", "Great App"])
    actual_reviews = set(result_df["review"].tolist())
    assert expected_reviews == actual_reviews
