import datetime

import bbox as bbox
import matplotlib.pyplot as plt
import sqlite3
from matplotlib import dates as dt
from matplotlib.widgets import Cursor
import numpy as np

x = [x for x in range(1, 20)]
y = [y ** 2 for y in range(1, 20)]
print(x, y)

fig = plt.figure()
ax = fig.subplots()
ax.plot(x, y)

cursor = Cursor(ax, horizOn=False, vertOn=False, useblit=True, color = 'r', linewidth= 1)

#createing and anothing box

# annot = ax.annotate('', xy=(0, 0), xytext=(-40, 40), textcoords='offset points',
#                     bbox=dict(boxstyle='round4', fc='linen', ec='k', lw=1),
#                     arrowprops=dict(arrowstyle='-|>'))

annot = ax.annotate('', xy=(0, 0), xytext=(-40, 40), textcoords='offset points',
                    bbox=dict(boxstyle='round4', fc='linen', ec='k', lw=1))
annot.set_visible(True)

coord = []
def onclick(event):
    global coord
    # coord.append((event.xdata, event.ydata))
    x= event.xdata
    y = event.ydata
    # print([x, y])
    annot.xy = (x,y)
    # text = f"{x, y}"
    text = '({:.2g}, {:.2g})'.format(x, y)
    annot.set_text(text)
    annot.set_visible(True)
    fig.canvas.draw()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
