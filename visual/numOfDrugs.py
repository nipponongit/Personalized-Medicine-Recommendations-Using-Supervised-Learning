#top 10 reasons and count unique drugs per reason
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("medicine.csv")
top_reasons = df['Reason'].value_counts().head(10)

top_reason_drugs = df[df['Reason'].isin(top_reasons.index)].groupby('Reason')['Drug_Name'].nunique()


plt.figure(figsize=(10, 6))
sns.barplot(x=top_reason_drugs.values, y=top_reason_drugs.index, palette="magma")
plt.title("Number of Unique Drugs for Top 10 Reasons")
plt.xlabel("Number of Unique Drugs")
plt.ylabel("Reason")
plt.tight_layout()
plt.show()
