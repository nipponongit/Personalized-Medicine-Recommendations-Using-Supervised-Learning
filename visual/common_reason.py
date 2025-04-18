import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("cleaned_filled_medicine.csv")


top_reasons = df['Reason'].value_counts().head(10)


plt.figure(figsize=(10, 6))
sns.barplot(x=top_reasons.values, y=top_reasons.index, palette="viridis")
plt.title("Top 10 Most Common Reasons for Prescription")
plt.xlabel("Count")
plt.ylabel("Reason")
plt.tight_layout()
plt.show()
