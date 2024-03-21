import http.client
import json
import pandas as pd
conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "fe586ed09cmsh88973b142689101p1a622ajsn10a8ef49fb25",
    'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
}

conn.request("GET", "/forecast/minutely?lat=35.5&lon=-78.5", headers=headers)

res = conn.getresponse()
data = res.read().decode('utf-8')

json_obj=json.dumps(data)

with open (r"C:\git\rohit958\WeatherData\data\weather_data.json",'w') as file:
    if file.write(json_obj):
        print('file created')
    else:
        print('writing failed')
