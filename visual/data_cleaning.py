import pandas as pd
import numpy as np


df = pd.read_csv("medicine.csv")


#Delete unnecessary columns (e.g., Unnamed columns)
df_cleaned = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df['Reason'] = df['Reason'].replace("Migraine", "Headache")
df['Reason'] = df['Reason'].replace("Viral", "Cold")
df.to_csv("updated_medicine.csv", index=False)

# Step 2: Keep only the relevant columns
relevant_columns = ['Drug_Name', 'Reason', 'Description', 'mildness']
df_final = df_cleaned[relevant_columns]

# Step 3: Fill missing 'mildness' values using logic based on 'Description'
def infer_mildness(description):
    if pd.isna(description):
        return 'moderate'
    description_lower = description.lower()
    if 'severe' in description_lower or 'strong' in description_lower:
        return 'severe'
    elif 'mild' in description_lower or 'light' in description_lower:
        return 'mild'
    elif 'moderate' in description_lower:
        return 'moderate'
    else:
        return 'moderate'


df_final['mildness'] = df_final.apply(
    lambda row: infer_mildness(row['Description']) if pd.isna(row['mildness']) else row['mildness'],
    axis=1
)


df_final.to_csv("cleaned_filled_medicine.csv", index=False)

print("✅ Data cleaned and saved as 'cleaned_filled_medicine.csv'")
