import urllib.request as a
import json as simplejson
import pandas as pd
import numpy as np
from urllib.error import HTTPError

api_key='83357010e805049f8a9d009658c7c1f0'
#d=a.urlopen("https://api.openweathermap.org/data/2.5/weather?q=pune,india&units=metric&appid=83357010e805049f8a9d009658c7c1f0")
#print(d.read())

s=input("enter city--")
city=s.replace(" ","%20")

url='https://api.openweathermap.org/data/2.5/weather?'
final_url=url+'q='+str(city)+'&units=metric&appid='+api_key
while True:
    try:
         json_obj=a.urlopen(final_url)
         break

    except (HTTPError,NameError):
        print("CITY NOT FOUND")
        exit()
data=simplejson.load(json_obj)

ins1=[data['name'],data["weather"][0]["description"],str(data["main"]["temp"])+"°C"]
df1=pd.DataFrame(np.array([ins1]),columns=["CITY_NAME","WEATHER","TEMPERATURE(°C)"],index=["➼"])

ins2=[data["name"],data["weather"][0]["description"],str(data["main"]["temp_max"])+"°C",str(data["main"]["temp_min"])+"°C",str(data["main"]["humidity"])+"%",str(data["wind"]["speed"])+"m/s"]

df2=pd.DataFrame(np.array([ins2]),columns=["CITY_NAME","WEATHER"," MAX_TEMP","MIN_TEMP","HUMIDITY","WIND_SPEED"],index=["➼"])

print(df1)
ch=input("‣‣‣‣‣‣‣DO YOU WANT MORE DETAILS? TYPE YES OR NO‣‣‣‣‣‣‣\t")
ch=ch.lower()
if ch=='y' or ch=='yes':
    print(df2)
    print("\n\n⦿⦿⦿Thank You⦿⦿⦿")

else:
    print("⦿⦿⦿Thank You⦿⦿⦿")

