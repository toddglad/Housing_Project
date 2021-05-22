# print("hello world")


import pandas as pd
# import googlemaps
from datetime import datetime
from itertools import tee
import json
# hello = 'Hello Todd'[::-1]



# print(hello)
# print("It worked")

df  = pd.read_csv(r'C:\Users\twade\Desktop\Housing Project\ChurchofJesusChristTemples.csv',engine = 'python')
# gmaps = googlemaps.Client(key='AIzaSyAIFjhJ68houXa379poru_HMRHpxrRzrY4')

# print(df)

# def pairwise(iterable):
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)

# #empty list - will be used to store calculated distances
list = []
list1 = []

# # Loop through each row in the data frame using pairwise
# for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
#       #Assign latitude and longitude as origin/departure points
#       LatOrigin = row1['Latitude'] 
#       LongOrigin = row1['Longitude']
#       origins = (LatOrigin,LongOrigin)

#       #Assign latitude and longitude from the next row as the destination point
#       LatDest = row2['Latitude']   # Save value as lat
#       LongDest = row2['Longitude'] # Save value as lat
#       destination = (LatDest,LongDest)

#       #pass origin and destination variables to distance_matrix function# output in meters
#       result = gmaps.distance_matrix(origins, destination, mode='driving', units = 'imperial')["rows"][0]["elements"][0]
#       #append result to list
#       list.append(result["distance"]["text"])
#       list1.append(result["duration"]["text"])
#       print(result["distance"]["text"])


# a = 0
# list.insert(a,0)
# list1.insert(a,0)
# df["Distance"] = list
# df["Duration"] = list1
# print(df)
####### This stuff all works.  Just working on the next portion.  

df1 = pd.read_csv(r'C:\Users\twade\Desktop\Housing Project\Housing_Project\uscities.csv',engine = 'python')
print(df1.head())


for (i1,row1) in df1.iterrows(): ## There is problem here with only having i1, row1
     LatOrigin = row1['lat'] 
     LongOrigin = row1['lng']
     origins = (LatOrigin,LongOrigin)
     print(origins)



