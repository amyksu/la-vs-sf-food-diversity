# LA vs SF - What city really does have the most diverse restaurant scene?
Using the Yelp API and the USA Today Diversity Index, analyzed whether Los Angeles or San Francisco has a more diverse food scene.

## Problem Statement

A point of contention between my NorCal friends and I is our opinions on the two cities’ foods. I am and have always been of the mindset that because LA spans such a large area and there are so many pockets of cultural hubs, we would have the more diverse restaurant scene. My SF friends argue that the scene up there is just better (not a great argument, but so be it), and therefore, not only would the food itself be better, but the diversity of the cuisines would also be better. With this in mind, I decided to back my argument up with some data to truly see if LA or SF has the most diverse cuisine. 

## Data Source

  - Data was sourced from [Yelp's API](https://www.yelp.com/developers) 
  
## Analytical Approach

See [my blog post](https://amyksu.com/blog/la-vs-sf-food-diversity#Pero-why) for full write up and 
[my jupyter notebook](https://github.com/amyksu/la-vs-sf-food-diversity/blob/master/LA%20vs%20SF%20Food%20Diversity%20Analysis.ipynb) for all code used for analysis. 

## Results and Conclusion

From the data and my calculations, I found the following: 
  - Based on the USA Today Diversity Index, SF’s food scene is more diverse than LA’s food scene. 
    - This slight difference can be attributed to the fact that SF has 60 unique ethnic cuisines as opposed to LA which has 59.
  - Almost a quarter of SF’s food scene (20.9%) is made up of American restaurants. 
  - The top 3 cuisines in LA, Mexican, American, and Korean, make up a little less than half of LA’s restaurant scene at 17.7%, 16.2%, and 12.8%, respectively. 
  - After combining cuisines that made up less than 1% of the distribution, LA had a greater diversity of cuisines, 17 include ‘Other’, while SF had 16 including “Other”. 

Please see [my jupyter notebook](https://github.com/amyksu/la-vs-sf-food-diversity/blob/master/LA%20vs%20SF%20Food%20Diversity%20Analysis.ipynb) for full conclusion and results. 

