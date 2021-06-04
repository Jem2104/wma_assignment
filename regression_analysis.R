setwd("C:/Users/jrlig/PycharmProjects/web-scraping")

library(ggplot2)
library(stargazer)

df <- read.csv('reviews.csv', header = TRUE, sep = ",", row.names=1)

df_restaurants <- unique(df[c('name_business', 'url', 'mean_rating', 'total_reviews',
                     'claimed_status', 'price_cat', 'categories', 'tot_n_photos',
                     'health_score', 'cov_updates', 'st_address')])

df_reviews  <- df[c('username', 'rating', 'date_review', 'text', 
                    'reviewer_city', 'reviewer_state', 'useful_votes', 
                    'funny_votes', 'cool_votes', 'n_photos', 'r_friends',
                    'r_reviews', 'r_photos', 'elite_tag', 'total_votes', 
                    'length_text')]

stargazer(df_restaurants, title = "Summary Statistics Businesses", 
          align = TRUE, no.space = TRUE, 
          intercept.bottom = FALSE, type = "text", 
          omit.summary.stat = c("p25", "p75"), 
          notes = "Note: N = Number of observations, Std. Dev. = Standard deviation.", 
          out = "Summary Statistics Businesses.html",
          order = c('mean_rating' ,'total_reviews', 'price_cat', 'tot_n_photos', 
                    'claimed_status', 'health_score'),
          omit = c('name_business', 'url', 'categories', 'cov_updates', 'st_address')) 

stargazer(df_reviews, title = "Summary Statistics Reviews", 
          align = TRUE, no.space = TRUE, 
          intercept.bottom = FALSE, type = "text", 
          omit.summary.stat = c("p25", "p75"), 
          notes = "Note: N = Number of observations, Std. Dev. = Standard deviation.", 
          out = "Summary Statistics Reviews.html",
          #order = c(2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16),
          omit = c(1, 3, 4, 5, 6))

lm1 <- lm(formula = total_votes ~ rating + n_photos + r_friends + r_reviews +
          r_photos + elite_tag + length_text, data = df_reviews)

lm2 <- lm(formula = useful_votes ~ rating + n_photos + r_friends + r_reviews +
            r_photos + elite_tag + length_text, data = df_reviews)

lm3 <- lm(formula = funny_votes ~ rating + n_photos + r_friends + r_reviews +
            r_photos + elite_tag + length_text, data = df_reviews)

lm4 <- lm(formula = cool_votes ~ rating + n_photos + r_friends + r_reviews +
            r_photos + elite_tag + length_text, data = df_reviews)

stargazer(lm1, title = "Regression", type = "text",
          out = "Regression Test.html")

stargazer(lm1, lm2, lm3, lm4, title = "Linear Regression Results",
          type = "text",
          out = "Regression Results.html")
