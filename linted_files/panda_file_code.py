"""Module for cleaning and preprocessing a pandas DataFrame."""

import pandas as pd

# Read the CSV file
df = pd.read_csv(
    r'C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\panda_file.csv',
    low_memory=False
)

# Fill NaNs for different data types and handle zip codes
for column in df.columns:
    if df[column].dtype == float:
        df[column].fillna(0, inplace=True)
    elif df[column].dtype == object:
        df[column].fillna('Unknown', inplace=True)

# Convert zip codes to string with leading zeros
if 'zip_code' in df.columns:
    df['zip_code'] = df['zip_code'].apply(
        lambda x: str(int(x)).zfill(5) if pd.notnull(x) else x
    )

# Replace pseudo NaNs with 'Unknown'
pseudo_nans = ['N/A', 'None', 'NaN']
df.replace(pseudo_nans, 'Unknown', inplace=True)

# Ensure zip_code is of string type
if 'zip_code' in df.columns:
    df['zip_code'] = df['zip_code'].astype(str)

# Write the cleaned DataFrame to a new CSV file
df.to_csv(
    r'C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\cleaned_panda_file.csv',
    index=False
)
