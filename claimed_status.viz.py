import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('memphis_reviews_updated.csv')

df = df[['claimed_status', 'rating']]
df = df.groupby(['claimed_status'], as_index=False).mean()

x, y = df['claimed_status'], df['rating']

y_pos = np.arange(len(x))
plt.bar(y_pos, y, align='center')
plt.xticks(y_pos, ['Not claimed', 'Claimed'])
plt.ylabel('Average rating')
plt.title('Average rating for claimed status')
axes = plt.gca()
axes.set_ylim([0, 5])
plt.savefig('bar_chart_claimed_status')
plt.show()
