import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("cleaned_filled_medicine.csv")
mildness_numeric = df['mildness'].astype('category').cat.codes


x = np.random.normal(loc=0, scale=0.1, size=len(df)) + mildness_numeric

plt.figure(figsize=(10, 6))
sns.scatterplot(x=x, y=mildness_numeric, hue=df['mildness'], palette='pastel', s=100, edgecolor='gray')

plt.yticks(ticks=range(len(df['mildness'].unique())), labels=df['mildness'].unique())
plt.xlabel('Spread (Randomized)')
plt.ylabel('Mildness Categories')
plt.title('Scatter Plot of Medicine Mildness', fontsize=16, fontweight='bold')
plt.grid(True)
plt.legend(title='Mildness', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
