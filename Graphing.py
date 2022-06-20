import datetime
import matplotlib.pyplot as plt
import sqlite3
from matplotlib import dates as dt
from matplotlib.widgets import Cursor
plt.style.use('ggplot')

con = sqlite3.connect("testing.db")
cur = con.cursor()

# WindAverage Grabbing
sql = "select WindAvg from weather"
cur.execute(sql)
WindAvgList = []
results = cur.fetchall()
for result in results:
    WindAvgList.append(float(result[0]))
# end

# WindGustList Grabbing
sql = "select WindGust from weather"
cur.execute(sql)
WindGustList = []
results = cur.fetchall()
for result in results:
    WindGustList.append(float(result[0]))
# end

# Wind Lull List Grabbing
sql = "select WindLull from weather"
cur.execute(sql)
WindLullList = []
results = cur.fetchall()
for result in results:
    WindLullList.append(float(result[0]))
# end

# Date Time Grabbing
spl = 'select Time from weather'
cur.execute(spl)
TimeList = []
results = cur.fetchall()
for result in results:
    # TimeList.append(float(result[0]))
    time = datetime.datetime.fromtimestamp(float(result[0]))
    TimeList.append(time)
# end

# making range
today = datetime.datetime.today()
morning = today.replace(hour=0, minute=0, second=0)
night = today.replace(hour=23, minute=59, second=59)
#end

#ploting
fig = plt.figure()
ax = fig.subplots()
ax.plot(TimeList, WindAvgList, "-r", label="Wind Average")
ax.plot(TimeList, WindGustList, "-b", label="Wind Gust")
ax.plot(TimeList, WindLullList, "-g", label='Wind Lull')
ax.legend(loc="upper left")

#formatting

plt.ylim([0, 45])
plt.xlim(morning, night)
date_format = dt.DateFormatter('%I:%M')
plt.gca().xaxis.set_major_formatter(date_format)
plt.title(f'{today.strftime("%B, %d, %Y")}')
plt.xlabel("Time")
plt.ylabel('Knots')
plt.gca().xaxis.set_major_locator(dt.HourLocator(interval=1))
plt.show()
