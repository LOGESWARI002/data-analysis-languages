# 🌍 Language Dataset Preprocessing

This project performs preprocessing and visualization on a dataset of languages and their codes.

- `language.csv`: The raw dataset containing language codes and names.
- `lang.py`: Python script for preprocessing and visualizing the dataset.
- `output 1.png` & `output 2.png`: Visual outputs showing the top 10 most common languages.

## 🧪 Dataset Description

The dataset has two columns:
- `Code`: Short language code (e.g., `en`, `fr_FR`)
- `Name`: Full language name, sometimes including region (e.g., `French (France)`)

Total entries: **239**

## 🧹 Preprocessing Steps

1. Load the dataset using pandas.
2. Remove duplicates.
3. Check for and report null values.
4. Split the `Name` column into:
   - `Language` (base language)
   - `Region` (if present, extracted from parentheses)
5. Count occurrences of each language (ignoring region).

## 📊 Visualization

A bar graph displays the **top 10 most common base languages** using seaborn.  
Example:  
![Top Languages](output%201.png)

## 🛠 Dependencies

Make sure to install the following Python libraries:

```bash
pip install pandas matplotlib seaborn
▶️ How to Run
Run the script using:

bash
Copy
Edit
python lang.py
📌 Output Preview
Terminal output:

Dataset info

First 5 rows

Duplicates and null check

Processed sample

Graphical output:

Bar chart of most common base languages.

This project is useful for understanding multilingual datasets and how to separate languages from locale codes.
