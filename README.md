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

This brings to question, what really is diversity? Is it having the most amount of different and unique cuisines? Or is it having a more evenly distributed food scene that is made up of multiple unique ethnic cuisines. Though LA is made up mostly of 3 cuisines, LA also has a greater percentage of diverse cuisines that make up more than 1% of the food scene, which in my opinion, means that LA has a slightly more diverse restaurant scene, but that could also be my bias talking. 

As with everything in life, what I have found is up to interpretation, but, based on my original method of determination, the USA Today Diversity Index, **SF is more diverse**. 

## Limitations

Because my project was limited in scope and information, this is just a sample of a full population that could be studied between SF and LA. With more information, it would be interesting to see how the distribution of each cuisine across a map of LA and SF and how that reflects the neighborhoods within each city. I would have also liked to have used Census data to compare the diversity of both LA and SF to see if the food diversity is an accurate reflection of the actual cities’ population diversity as well. 

## Future Work

Other interesting things I wish I could have done: 

  - An analysis of the food scene over time. Has SF/LA gotten more or less diverse over time?
  - An analysis on food price. What is the distribution of restaurants at different price points and what does that say about the people who frequent those places? What is the difference of these distributions in both SF and LA and what does this mean about the two cities? 
  - Was the Diversity Index really the best method? Sure I did my research, but I would maybe have tried a different approach to determining my question such as a chi-squared test. 

Please see [my jupyter notebook](https://github.com/amyksu/la-vs-sf-food-diversity/blob/master/LA%20vs%20SF%20Food%20Diversity%20Analysis.ipynb) for full analysis. 

