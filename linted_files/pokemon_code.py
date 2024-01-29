import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r'C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\pokemon.csv')


plt.figure(figsize=(20, 15))


avg_hp_by_type = df.groupby('type1')['hp'].mean().sort_values()
plt.subplot(2, 2, 1)
avg_hp_by_type.plot(kind='bar', color='skyblue')
plt.title('Average HP by Pokemon Type')
plt.ylabel('Average HP')
plt.xlabel('Type 1')

type_distribution = df['type1'].value_counts()
plt.subplot(2, 2,  2)
type_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pokemon Type 1 Distribution')

plt.subplot(2, 2, 3)
df['attack'].plot(kind='hist', bins=20, color='orange')
plt.title('Histogram of Pokemon Attack Ratings')
plt.xlabel('Attack Rating')
plt.ylabel('Number of Pokemon')

plt.subplot(2, 2, 4)
plt.scatter(df['attack'], df['defense'], alpha=0.5, c='green')
plt.title('Attack vs. Defense Scatter Plot')
plt.xlabel('Attack')
plt.ylabel('Defense')

plt.tight_layout()


plt.show()
