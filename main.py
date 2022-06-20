import requests
import json
import sqlite3
from datetime import datetime
from time import sleep


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


for y in range(1, 100):
    windAvg = []
    windGust = []
    WindLull = []
    WindDirection = []
    Time = []
    constant = 1.95
    for i in range(0, 3):
        response = requests.get(
            "https://swd.weatherflow.com/swd/rest/observations/station/74397?token=9d1e5ce4-e468-4935-85b6-0329d0feeb65")
        # print(response.json())
        # jprint(response.json())
        x = response.json()
        print(x['obs'][0]["wind_avg"])
        print(x['obs'][0]["wind_gust"])
        print(x['obs'][0]["wind_lull"])
        print(x['obs'][0]["wind_direction"])

        windAvg.append((x['obs'][0]["wind_avg"]) * constant)
        windGust.append((x['obs'][0]['wind_gust']) * constant)
        WindLull.append((x['obs'][0]['wind_lull']) * constant)
        WindDirection.append(x['obs'][0]['wind_direction'])
        Time.append(x['obs'][0]['timestamp'])
        print("done")
        sleep(60)
    AverageWindAvg = (sum(windAvg)) / len(windAvg)
    AverageWindGust = (sum(windGust)) / len(windGust)
    AverageWindLull = (sum(WindLull)) / len(WindLull)
    AverageWindDirection = WindDirection[2]
    AverageTime = Time[2]
    print(AverageWindAvg, AverageWindGust, AverageWindLull, AverageWindDirection, AverageTime)
    print(windAvg, windGust, WindLull, WindDirection, Time)
    con = sqlite3.connect("testing.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS weather (WindAvg text, WindGust text, WindLull, WindDirection, Time)")
    cur.execute("INSERT INTO weather VALUES(?, ?, ?, ?, ?)", (AverageWindAvg, AverageWindGust, AverageWindLull, AverageWindDirection, AverageTime))
    con.commit()