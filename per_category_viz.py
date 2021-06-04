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
# get the count per column
df.loc['total'] = df.sum()

# extract the top 10 categories
df = df.T
top_10 = list(df.nlargest(10, 'total').index.values)

# extract the bottom 10 categories
bottom_10 = list(df.nsmallest(10, 'total').index.values)

# get the average rating per category
df = df.T
df = df[:-1]
cols = df.columns

averages = []

for i in cols:
    df_cut = df.loc[df[i] == 1]
    averages.append(df_cut['mean_rating'].mean())

average_per_category_df = pd.DataFrame(
    {'mean_rating': averages,
     'category': cols}
)
average_per_category_df = average_per_category_df[1:]

# get the average rating for both top and bottom 10
average_per_category_df = average_per_category_df.sort_values('mean_rating', ascending=False)
top_10_with_rating = average_per_category_df.loc[average_per_category_df['category'].isin(top_10)]

average_per_category_df = average_per_category_df.sort_values('mean_rating', ascending=False)
bottom_10_with_rating = average_per_category_df.loc[average_per_category_df['category'].isin(bottom_10)]

# # Create the graphs
x, y = top_10_with_rating['category'], top_10_with_rating['mean_rating']

y_pos = np.arange(len(x))
plt.bar(y_pos, y, align='center')
plt.xticks(y_pos, x, rotation=50, ha='right')
plt.ylabel('Average rating')
plt.title('Average rating for top 10 most reviewed categories')
axes = plt.gca()
axes.set_ylim([0, 5])
# plt.savefig('average_rating_top_10_most_reviewed')
plt.show()

# x, y = bottom_10_with_rating['category'], bottom_10_with_rating['mean_rating']
#
# y_pos = np.arange(len(x))
# plt.bar(y_pos, y, align='center')
# plt.xticks(y_pos, x, rotation=50, ha='right')
# plt.ylabel('Average rating')
# plt.title('Average rating for top 10 least reviewed categories')
# axes = plt.gca()
# axes.set_ylim([0, 5])
# plt.savefig('average_rating_top_10_least_reviewed')
# plt.show()