import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("cleaned_filled_medicine.csv")


drug_counts = df.groupby(['Reason', 'Drug_Name']).size().reset_index(name='count')


top_reasons = df['Reason'].value_counts().head(5).index
filtered = drug_counts[drug_counts['Reason'].isin(top_reasons)]


pivot_df = filtered.pivot_table(index='Drug_Name', columns='Reason', values='count', fill_value=0)


pivot_df = pivot_df.head(20)


plt.figure(figsize=(14, 7))
pivot_df.plot(kind='line', marker='o', figsize=(14, 7), colormap='tab10')
plt.title("Line Graph: Drug Names vs Top 5 Reasons")
plt.xlabel("Drug Name")
plt.ylabel("Count (Occurrences)")
plt.xticks(rotation=45, ha='right')
plt.legend(title='Reason')
plt.tight_layout()
plt.show()
