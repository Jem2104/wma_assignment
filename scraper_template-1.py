# -*- coding: utf-8 -*-
"""
Created on Mon May 19 13:04:35 2021

@author: Kanellopoulos
"""
#### SCRAPER TEMPLAT
# This is a template of the crawler you learn to configure in the workshop.
# It has many of the functionalities that you learn in the videos already implemented.
# Please use the workshop videos to understand the parts of the scraper.
# However, you will see it does not contain the CSS-Selector information that we need for the soup.select funtions, for instance.
# Moreover, it does not contain all of the URLs. Needless to say, if the run the scraper template in the current form, it will throw
# errors due to missing information.
# You will need to insert these information yourselves.

################STEP 1: Motherlist

# Getting the restaurant list for Boston, MA
import requests
url = "https://www.yelp.com/search?cflt=restaurants&find_loc=Boston%2C%20MA&start=0"
html = requests.get(url)
html.content[0:500]

# Making the soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html.content, 'lxml')

# Identifying the restaurant links
links = soup.select(".css-1pxmz4g")
print(links[0:10])

# Getting the restaurant names and the restaurant links in solation
name_restaurant = []
link_restaurant = []

for link in links:
    name_restaurant.append(link.string)
    link_restaurant.append(link.get('href'))
    
print(name_restaurant[0:5])
print(link_restaurant[0:5])


# Getting everything also for multiple pages (here, for page 2, 3, 4, 5, and 6)
url_yelp = 

for j in range(1,5):
    
    html = requests.get(url_yelp + str(j*10))
    
    soup = BeautifulSoup(html.content, 'lxml')
    links = soup.select("")
   
    for link in links:
        name_restaurant.append(link.string)
        link_restaurant.append(link.get('href'))

# Making sure we have everything
print(name_restaurant)  
print(link_restaurant)

# Completing the restaurant links
link_restaurant=["https://www.yelp.com" + s for s in link_restaurant]
print(link_restaurant[0:5])
 

#Putting the restaurant list into a csv
import pandas as pd

RestaurantDataSet = list(zip(name_restaurant,link_restaurant))
df_restaurants = pd.DataFrame(data = RestaurantDataSet , columns=['name', 'url'])
#Show first ten rows
df_restaurants.iloc[:10]

df_restaurants.to_csv('boston_restaurants_from_website_workshop.csv',index=False,header=True,encoding='utf8')

################STEP 2: Going through the subpages

#collect variables for restaurants
url = df_restaurants['url'][1]
name_business = df_restaurants['name'][1]

html = requests.get(url)
soup = BeautifulSoup(html.content, 'lxml')

soup_username = soup.select('')
soup_username[1:5]

username = []

for name in soup_username:
    username.append(name.string)
    
username[0:5]

# Get ratings
soup_stars=soup.select('')
soup_stars[0:5]

rating = []

for stars in soup_stars:
    rating.append(stars.attrs['aria-label'])

rating[0:5]   

# Get rid of text "star rating"
import re
rating  = [re.sub(' star rating', '',  r) for r in rating]

#convert from string to number
rating = [float(i) for i in rating]

#Get date of rating
soup_date=soup.select('')
soup_date[0:5]

date_review = []

for date in soup_date:
    date_review.append(date.string)

date_review[0:5]

#Get the review text
html_texts=soup.select('')
html_texts[0:10]

html_text = []

for t in html_texts:
    html_text.append(t.get_text())

html_text

#Combine everything to dataset

#add name business
name_business_mult = [name_business] * len(username)
url_restaurant_mult = [url] * len(username)


RatingDataSet = list(zip(name_business_mult, url_restaurant_mult, username, rating, date_review, html_text))

df_rating = pd.DataFrame(data = RatingDataSet, columns=['name_business','url', 'username', 'rating', 'date_review', 'text'])
df_rating.iloc[:10]

df_rating.to_csv('boston_ratings_workshop.csv',index=False,header=True,encoding='utf8')

#####Step 3: Putting Step 2 in a loop

for u in range(1,5):
    try:            
        #collect variables for restaurants                                    
        url = df_restaurants['url'][u]
        name_business = df_restaurants['name'][u]
        
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'lxml')
        
        soup_username = soup.select('')
          
        username = []

        for name in soup_username:
            username.append(name.string)            

        # Get ratings
        soup_stars = soup.select('')

        rating = []

        for stars in soup_stars:
            rating.append(stars.attrs['aria-label'])
            
        # Get rid of text "star rating"
        import re
        rating  = [re.sub(' star rating', '',  r) for r in rating]

        #convert from string to number
        rating = [float(i) for i in rating]      
                
        #Get date of rating
        soup_date = soup.select('')

        date_review = []

        for date in soup_date:
            date_review.append(date.string)
            
        #Get the review text
        html_texts = soup.select('')
        
        html_text = []

        for t in html_texts:
            html_text.append(t.get_text())
                
        name_business_mult = [name_business] * len(username)
        url_restaurant_mult = [url] * len(username)

        RatingDataSet = list(zip(name_business_mult, url_restaurant_mult, username, rating, date_review, html_text))

        df_rating = pd.DataFrame(data = RatingDataSet, columns=['name_business', 'url', 'username', 'rating', 'date_review', 'text'])

        with open('boston_ratings150_workshop.csv', 'a',newline='') as f:
            df_rating.to_csv(f, index=False, header=False, encoding='utf8')
                
        print(u)
        import time
        time.sleep(2)
        
    except:
        print("A page was not loaded correctly")
