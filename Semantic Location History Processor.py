# Adapted from: https://towardsdatascience.com/analyzing-my-2020-google-location-history-data-516f4916258
import json
import datetime 
mst = datetime.timezone(datetime.timedelta(hours=-7))
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST',
            'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
full_year=[]

home = "1168 "
work = "10010"
for month in months:
    f = open(f'Semantic Location History/2022/2022_{month}.json', encoding='utf-8')
    data=json.load(f)
    address_list=[]
    
    for items in data.values():
        for item in items:
            if "placeVisit" in item:
                place = item['placeVisit']
                addr = place['location']['address']
                if '10010' not in addr:
                    continue
                start = datetime.datetime.fromisoformat(place['duration']['startTimestamp'])
                end = datetime.datetime.fromisoformat(place['duration']['endTimestamp'])
                duration = end - start

                print(f"{start.astimezone(mst).strftime('%b %d, %H:%M' )} {addr} TIME:{str(duration)}")

                    
    
