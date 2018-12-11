# code used to scrape Yelp API

import os
import csv
import itertools
import collections
from yelpapi import YelpAPI

# LA zip codes.
la_zip = ['90004','90005','90006','90007','90008','90010','90012','90013','90014','90015','90016','90017','90018','90019','90020','90021','90023','90024','90025','90026','90027','90028','90033','90034','90035','90036','90039','90042','90043','90046','90048','90049','90056','90057','90064','90065','90066','90067','90068','90069','90071','90077','90079','90094','90210','90211','90212','90230','90232','90291','90292','90401','90401','90402','90403','90405']

# SF zip codes (to add)
sf_zip = []

# 
# Flatten nested dictionaries.
# 

def flatten(d, parent_key='', sep='_'):
  items = []
  for k, v in d.items():
    new_key = parent_key + sep + k if parent_key else k
    if isinstance(v, collections.MutableMapping):
      items.extend(flatten(v, new_key, sep=sep).items())
    else:
      items.append((new_key, v))
  return dict(items)

# File to write.
file = csv.writer(open("businesses-los-angeles.csv", "w+", encoding="utf-8"))

# Initialize yelp client.
yelp_api = YelpAPI('Zxxx-xxxx-xxxx')


for zip_code in la_zip:
  limit = 50
  length = limit
  total = 0 
  offset = 0
  while length > 0:
    try:
      search_results = yelp_api.search_query(find_desc="restaurants", 
                                             location=zip_code,
                                             limit=limit,
                                             is_closed=False,
                                             offset=offset)
    except Exception as e:
      print("Error! {e}".format(e=e))
      break

    businesses = search_results['businesses']
    businesses = [business for business in businesses if business['location']['city'] == "Los Angeles"]
    businesses = [business for business in businesses if not business['is_closed']]

    if len(businesses) == 0:
      break

    if offset == 0:
      file.writerow(flatten(businesses[0]).keys())

    for business in businesses:
      file.writerow(flatten(business).values())

    total += len(businesses)
    offset += limit

    
file.close()
