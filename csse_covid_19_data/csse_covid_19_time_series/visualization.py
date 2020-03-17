import pandas as pd

df = pd.read_csv("time_series_19-covid-Confirmed.csv")

def extract_line(name):
    gerline = df[df["Country/Region"] == name]
    gerline = gerline.drop(columns=["Lat", "Long", "Country/Region", "Province/State"])
    gerline = gerline.T
    gerline.index = pd.to_datetime(gerline.index)
    colname = gerline.columns[0]
    gerline = gerline[colname]
    gerline.name=name
    return gerline

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import math

extrapolate_index = pd.date_range("2020-02-20", "2020-03-31")
a = 5
b = 0.3
extrapolate_data = np.array([a*math.exp(b*x) for x in range(len(extrapolate_index))])
df2 = pd.Series(index=extrapolate_index, data=extrapolate_data)


ax = plt.gca()
i = ["Italy", "Germany", "Switzerland", "Spain"]
for c in i:
    extract_line(c).plot(ax=ax)
    
df2.plot(ax=ax)
ax.legend(i)

plt.yscale("log")

plt.show()
