import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?cflt=restaurants&find_loc=Boston%2C%20MA&start="

name_restaurant = []
link_restaurant = []

for j in range(0, 24):
    html = requests.get(url + str(j*10))
    soup = BeautifulSoup(html.content, 'html.parser')
    links = soup.select('.css-1pxmz4g .css-166la90')

    for link in links:
        name_restaurant.append(link.string)
        link_restaurant.append(link.get('href'))

print(name_restaurant)
print(link_restaurant)

link_restaurant = ['https://www.yelp.com' + s for s in link_restaurant]
link_restaurant[0:5]

import pandas as pd
joined_list = list(zip(name_restaurant, link_restaurant))
df = pd.DataFrame(data=joined_list, columns=['name', 'url'])
df.head()