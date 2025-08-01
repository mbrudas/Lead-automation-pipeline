"""
Lead Cleaning Script
Cleans and standardizes a CSV dataset of leads:
- Removes duplicates
- Validates email format
- Normalizes phone numbers
- Standardizes column names
"""

import pandas as pd
import re

# Load raw dataset
df = pd.read_csv("customers_raw.csv")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop duplicate entries
df.drop_duplicates(inplace=True)

# Email validation function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Apply email filter
df = df[df['email'].apply(lambda x: is_valid_email(str(x)))]

# Normalize phone numbers
def normalize_phone(phone):
    digits = re.sub(r'\D', '', str(phone))
    return f"+{digits}" if digits.startswith("1") else f"+1{digits}"

df['phone'] = df['phone'].apply(normalize_phone)

# Save clean dataset
df.to_csv("customers_clean.csv", index=False)

print(f"✅ Dataset cleaned successfully: {len(df)} valid leads.")
