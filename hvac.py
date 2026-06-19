import os
import pandas as pd

folder = r"C:\Users\Owner\Downloads\archive"
csv_file = [f for f in os.listdir(folder) if f.endswith(".csv")][0]
file_path = os.path.join(folder, csv_file)

print("Loading file:", file_path)
df = pd.read_csv(file_path)

print(df.head())  # check it loaded right
print(df.columns)

print(df.isnull().sum())  # any gaps in the data?
print(df.describe())  # quick stats overview