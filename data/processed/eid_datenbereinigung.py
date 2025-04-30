import pandas as pd

file_path = r"C:\Users\chris\Corporate_Environmental_Impact\data\raw\Scope-3-Environmental-Impact-Data-2022.xlsx"

df = pd.read_excel(file_path, sheet_name="0%")

print(df.head())
df.shape
