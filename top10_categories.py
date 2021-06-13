import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

df = pd.read_csv('memphis_reviews_updated.csv')
df = df[['categories', 'mean_rating', 'url', 'name_business']]

# only keep one row for every company
df = df.groupby(['url'], sort=False).first().reset_index()

# clean the column names a bit
df['categories'] = df['categories'].str.replace(' ', '')
df['categories'] = df['categories'].str.replace("'", '')
df['categories'] = df['categories'].str.replace('[', '')
df['categories'] = df['categories'].str.replace(']', '')

# make all categories boolean columns
df = df.join(df['categories'].str.get_dummies(','))
df = df.drop(columns=['categories', 'name_business', 'url'])

df = df.drop('mean_rating', 1)

# get the count per column
df.loc['total'] = df.sum()

# extract the top 10 categories
df = df.T
top_10 = list(df.nlargest(10, 'total').index.values)

df = df.T
df = df[top_10].iloc[-1, :]
df.plot.bar()
plt.title('Top 10 most occurring restaurant categories')
plt.xticks(rotation=45, ha='right')
# plt.savefig('top_10_categories')
plt.show()