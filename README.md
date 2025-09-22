Task 1 — Data Cleaning & Preprocessing

I worked on the Netflix dataset from Kaggle.  
The goal was to clean and prepare the dataset for analysis.

 What I Did:
- Removed duplicate records  
- Filled missing values in `director`, `cast`, `country`, and `rating` with "Unknown"  
- Converted the `date_added` column into proper date format  
- Made sure `type` column has only "Movie" or "TV Show"  
- Cleaned `release_year` to be numeric only  

 Files in This Repository:
- Raw dataset → netflix_titles_nov_2019.csv  
- Cleaned dataset → netflix_cleaned.csv  
- Python script → cleaned_netflix.py
-  Documentation → README.md
