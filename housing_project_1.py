print("hello world")



import pandas as pd
import googlemaps
from datetime import datetime
from itertools import tee
import json
hello = 'Hello Todd'[::-1]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



print(hello)
print("It worked")

df  = pd.read_csv(r'C:\Users\twade\Desktop\Housing Project\ChurchofJesusChristTemples.csv',engine = 'python')
gmaps = googlemaps.Client(key='AIzaSyAIFjhJ68houXa379poru_HMRHpxrRzrY4')

print(df)

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#empty list - will be used to store calculated distances
list = []

# Loop through each row in the data frame using pairwise
for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
      #Assign latitude and longitude as origin/departure points
      LatOrigin = row1['Latitude'] 
      LongOrigin = row1['Longitude']
      origins = (LatOrigin,LongOrigin)

      #Assign latitude and longitude from the next row as the destination point
      LatDest = row2['Latitude']   # Save value as lat
      LongDest = row2['Longitude'] # Save value as lat
      destination = (LatDest,LongDest)

      #pass origin and destination variables to distance_matrix function# output in meters
      result = gmaps.distance_matrix(origins, destination, mode='driving', units = 'imperial')["rows"][0]["elements"][0]
      #append result to list
      list.append(result["distance"]["text"])
      print(result["distance"]["text"])

df['Distance']=list
print("here")
# 
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# destination = (40.6943, -73.9249)
# actual_duration = []

# destinations = df[['Latitude', 'Longitude']]


# test = destinations.head()
# for destination in destinations:
#     result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["duration"]["value"]  
#     result = result/3600
#     actual_duration.append(result)



### This is a test
## This is another test
