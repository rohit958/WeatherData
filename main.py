import pandas as pd
import json
from pandasql import sqldf

with open(r"C:\git\rohit958\WeatherData\data\weather_data.json",encoding='utf-8', errors='ignore') as f:
    json_obj=json.loads(f.read(),strict=False)


#creating pandas dataframe
df=pd.read_json(json_obj)
print(df.head(3))

destination=r"C:\git\rohit958\WeatherData\final_csv\final.csv"
try:
    df.to_csv(destination,sep='|',header=True,index=True)
    print('file created')
except FileExistsError:
    print('failed')
finally:

    print("exting")
    exit()
