# Customer Experience Analytics for Fintech Apps

This project processes customer reviews of Ethiopian fintech mobile banking apps to uncover **user sentiment**, **pain points**, and **themes** that help improve product and service quality.

---

## Task 1: Data Cleaning and Preprocessing

###  Objective:
To standardize and clean raw review data collected from multiple CSV files, removing inconsistencies and preparing it for analysis.

### What We Did:

- Combined multiple raw review files.
- Standardized column names.
- Cleaned and normalized date formats.
- Removed missing and duplicate values.
- Trimmed whitespace and corrected formats.

###  Steps Followed:

1. **Load All CSV Files**  
   Used `glob` to find all files matching `*_reviews_*.csv`.

2. **Standardize Column Names**  
   Renamed:
   - `review_text` → `review`
   - `bank_name` → `bank`

3. **Normalize Dates**  
   Converted all `date` values to `YYYY-MM-DD` format.

4. **Drop Incomplete Rows**  
   Removed rows missing critical fields: `review`, `rating`, `date`, `bank`, `source`.

5. **Remove Whitespace**  
   Stripped unnecessary whitespace from `review`, `bank`, and `source`.

6. **Remove Duplicates**  
   Removed exact duplicates based on `review`, `date`, and `bank`.

7. **Output**  
   Cleaned reviews saved into:
