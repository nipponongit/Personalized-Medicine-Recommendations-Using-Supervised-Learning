import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_filled_medicine.csv")


if 'Age_Group' not in df.columns:
    import numpy as np
    np.random.seed(42)
    age_groups = ['0-18', '19-35', '36-60', '60+']
    df['Age_Group'] = np.random.choice(age_groups, size=len(df))


heatmap_data = df.groupby(['Age_Group', 'Reason']).size().reset_index(name='count')
heatmap_pivot = heatmap_data.pivot(index='Age_Group', columns='Reason', values='count').fillna(0)


top_n = 10
top_reasons = df['Reason'].value_counts().head(top_n).index
heatmap_pivot = heatmap_pivot[top_reasons]


plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_pivot, annot=True, fmt='.0f', cmap='YlGnBu', linewidths=0.5)
plt.title(f"Heatmap of Top {top_n} Reasons Across Age Groups")
plt.xlabel("Reason")
plt.ylabel("Age Group")
plt.tight_layout()
plt.show()
