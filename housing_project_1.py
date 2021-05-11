# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





import pandas as pd
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyAIFjhJ68houXa379poru_HMRHpxrRzrY4')

reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

##import pandas as pd
## df  = pd.read_csv(r'C:\Users\twade\Desktop\Housing Project\city_temperature.csv',engine = 'python')
##print(df)


### This is a test
## This is another test
