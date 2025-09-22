import pandas as pd
import numpy as np

# 1. Load dataset
df = pd.read_csv(r"D:\task1-netflix-cleaning\netflix_titles_nov_2019.csv")

print("Initial Shape:", df.shape)

# 2. Remove duplicates
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# 3. Handle missing values
for col in ['director', 'cast', 'country', 'rating']:
    df[col] = df[col].fillna('Unknown')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['type'] = df['type'].str.strip().str.title()
df['country'] = df['country'].str.strip()

df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

print("Missing values:\n", df.isnull().sum())

df.to_csv(r"D:\task1-netflix-cleaning\netflix_cleaned.csv", index=False)
print("✅ Cleaned dataset saved as netflix_cleaned.csv")
