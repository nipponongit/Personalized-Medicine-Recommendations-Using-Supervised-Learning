import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patheffects as path_effects


file_path = 'cleaned_filled_medicine.csv'
df = pd.read_csv(file_path)
df.columns = df.columns.str.lower().str.strip()


if 'mildness' not in df.columns:
    raise ValueError("The 'mildness' column is missing.")

df['mildness'] = df['mildness'].astype(str).str.strip().str.title()
mildness_counts = df['mildness'].value_counts()
labels = mildness_counts.index.tolist()
sizes = mildness_counts.values.tolist()


labels_with_counts = [f"{label} ({count})" for label, count in zip(labels, sizes)]


colors = sns.color_palette("Spectral", len(labels))  # Gradient style
explode = [0.08] * len(labels)  # Pop out all slices slightly
shadow_color = 'gray'


plt.style.use('seaborn-v0_8-poster')
fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    pctdistance=0.8,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)


for i, text in enumerate(texts):
    text.set_fontsize(10)
for i, autotext in enumerate(autotexts):
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_path_effects([path_effects.Stroke(linewidth=1.2, foreground='white'), path_effects.Normal()])

ax.legend(wedges, labels_with_counts,
          title="Mildness Levels",
          loc="center left",
          bbox_to_anchor=(1, 0.5),
          fontsize=10,
          title_fontsize=12,
          frameon=True,
          shadow=True)


plt.title("🌡️ Distribution of Drugs by Mildness Level", fontsize=18, fontweight='bold', pad=20)
ax.axis('equal')  
plt.tight_layout()
plt.show()
