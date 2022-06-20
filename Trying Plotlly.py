import datetime
import sqlite3
from bokeh.models import DatetimeTickFormatter, Range1d, HoverTool
from bokeh.plotting import figure, show, ColumnDataSource

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
# end

source = ColumnDataSource(data={
    'TimeList': TimeList,
    "WindAvgList": WindAvgList,
    "WindGustList": WindGustList,
    'WindLullList': WindLullList
})

# ploting
p = figure(title=today.strftime('%B, %d, %Y'), x_axis_label='Time', y_axis_label='Knots', x_axis_type='datetime',
           plot_width=1500, plot_height=800, tools='')
p.circle(TimeList, WindAvgList)
p.line(x="TimeList", y="WindAvgList", legend_label='Wind Average', source=source)
p.add_tools(HoverTool(
    tooltips=[
        ('Wind Average', "@WindAvgList"),
        ('Wind Gust', '@WindGustList'),
        ('Wind Lull', '@WindLullList')
    ]
))

# formatting
p.x_range = Range1d(morning, night)
p.y_range = Range1d(0, 45)
p.xaxis[0].formatter = DatetimeTickFormatter(hours='%I:%M', hourmin='%I:%M', minutes='%I:%M')
hover = HoverTool(tooltips="Time @TimeList")
show(p)
