

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load dataset
df = pd.read_csv("language.csv")

# Basic info
print("Initial Data Info:")
print(df.info())
print("\nFirst 5 rows:\n", df.head())

# Check for duplicates
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Check for null values
print("\nMissing values:\n", df.isnull().sum())

# Feature engineering: split name and region (if any)
df['Language'] = df['Name'].apply(lambda x: re.sub(r'\(.*\)', '', x).strip())
df['Region'] = df['Name'].apply(lambda x: re.search(r'\((.*?)\)', x).group(1) if re.search(r'\((.*?)\)', x) else pd.NA)

# Count languages (without regions)
language_counts = df['Language'].value_counts().head(10)

# Plot top 10 most frequent languages
plt.figure(figsize=(10, 5))
sns.barplot(x=language_counts.values, y=language_counts.index, palette='viridis')
plt.title('Top 10 Most Common Languages in Dataset')
plt.xlabel('Count')
plt.ylabel('Language')
plt.tight_layout()
plt.show()

# Final processed dataset preview
print("\nProcessed Data Sample:\n", df.head())

