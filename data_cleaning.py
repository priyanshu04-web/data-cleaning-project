import pandas as pd

df = pd.read_csv("dataset/raw_dataset_with_issues.csv")

print("Missing values before:", df.isna().sum().sum())
print("Duplicate rows before:", df.duplicated().sum())

df = df.drop_duplicates().copy()

numeric_cols = [
    "sepal_length_cm", "sepal_width_cm",
    "petal_length_cm", "petal_width_cm"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["sepal_width_cm"] = df["sepal_width_cm"].fillna(
    df["sepal_width_cm"].median()
)

df["species"] = (
    df["species"]
    .astype("string")
    .str.strip()
    .str.lower()
)

df.to_csv("dataset/cleaned_dataset.csv", index=False)

print("Missing values after:", df.isna().sum().sum())
print("Duplicate rows after:", df.duplicated().sum())
