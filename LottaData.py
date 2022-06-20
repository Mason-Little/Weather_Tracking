import requests
import json
import sqlite3
from datetime import datetime
from time import sleep


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

constant = 1.93

for i in range(0, 100):
    response = requests.get(
        "https://swd.weatherflow.com/swd/rest/observations/station/74397?token=9d1e5ce4-e468-4935-85b6-0329d0feeb65")
    # print(response.json())
    # jprint(response.json())
    x = response.json()
    print(x['obs'][0]["wind_avg"])
    print(x['obs'][0]["wind_gust"])
    print(x['obs'][0]["wind_lull"])
    print(x['obs'][0]["wind_direction"])

    windAvg = ((x['obs'][0]["wind_avg"]) * constant)
    windGust = ((x['obs'][0]['wind_gust']) * constant)
    WindLull = ((x['obs'][0]['wind_lull']) * constant)
    WindDirection = (x['obs'][0]['wind_direction'])
    Time = (x['obs'][0]['timestamp'])
    print("done")
    con = sqlite3.connect("testing.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS weather (WindAvg text, WindGust text, WindLull, WindDirection, Time)")
    cur.execute("INSERT INTO weather VALUES(?, ?, ?, ?, ?)", (windAvg, windGust, WindLull, WindDirection, Time))
    con.commit()
    sleep(60)
