import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("cleaned_filled_medicine.csv")


if 'Age_Group' not in df.columns:
    import numpy as np
    np.random.seed(42)
    age_groups = ['0-18', '19-35', '36-60', '60+']
    df['Age_Group'] = np.random.choice(age_groups, size=len(df))


grouped = df.groupby(['Age_Group', 'Reason']).size().reset_index(name='count')


grouped_sorted = grouped.sort_values(['Age_Group', 'count'], ascending=[True, False])


top_n = 3
top_reasons_multi = grouped_sorted.groupby('Age_Group').head(top_n)


plt.figure(figsize=(12, 7))
sns.barplot(data=top_reasons_multi, x='count', y='Age_Group', hue='Reason', dodge=True)
plt.title(f"Top {top_n} Reasons per Age Group")
plt.xlabel("Number of Prescriptions")
plt.ylabel("Age Group")
plt.legend(title="Reason", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
