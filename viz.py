import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('memphis_reviews_updated.csv')

df['length'] = df['text'].str.count(' ') + 1
# df['average_per_length'] = df.groupby('length')['rating'].transform('mean')

df = df[['length', 'rating']]
df = df.groupby(['length'], as_index=False).mean()

# binning them boys
bins = np.arange(0, 1000, 25)
df = df.groupby(pd.cut(df['length'], bins=bins))['rating'].agg(['mean'])
df['length'] = bins[:-1]

x, y = df['length'], df['mean']
plt.plot(x, y, 'o')

# adding a regression line
b, m = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, '-')

plt.title('Average rating per binned length with steps of 25')
plt.xlabel('Length of review')
plt.ylabel('Average rating')
# plt.savefig('average_rating_per_length_binned')
plt.show()