print("hello world")



import pandas as pd
import googlemaps
from datetime import datetime
from itertools import tee
hello = 'Hello Todd'[::-1]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



print(hello)
print("It worked")

df  = pd.read_csv(r'C:\Users\twade\Desktop\Housing Project\ChurchofJesusChristTemples.csv',engine = 'python')
gmaps = googlemaps.Client(key='AIzaSyAIFjhJ68houXa379poru_HMRHpxrRzrY4')
origin = (2.01234699405899,29.377851313693)
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
destination = (40.6943, -73.9249)
actual_duration = []

destinations = df[['Latitude', 'Longitude']]


test = destinations.head()
for destination in destinations:
    result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["duration"]["value"]  
    result = result/3600
    actual_duration.append(result)




### This is a test
## This is another test
