import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('memphis_reviews_updated.csv')

df['length'] = df['text'].str.count(' ') + 1
# df['average_per_length'] = df.groupby('length')['rating'].transform('mean')

df = df[['length', 'rating']]
df = df.groupby(['length'], as_index=False).mean()
print(df.head())

plt.plot(df['length'], df['rating'])
plt.title('Average rating per length')
plt.xlabel('Length of review')
plt.ylabel('Average rating')
plt.savefig('average_rating_per_length')
plt.show()