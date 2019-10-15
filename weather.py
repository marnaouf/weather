import numpy as np
import pandas as pd
import plotly.express as px


d = pd.read_csv('beirut.csv', parse_dates=['date_time'])
d = d.set_index('date_time')
data = pd.DataFrame()
r = d.tempC.resample('W')
data['tempC'] = r.mean()
data['minTempC'] = r.min()
data['maxTempC'] = r.max()
data['range_max'] = data['maxTempC'] - data['tempC']
data['range_min'] = data['tempC'] - data['minTempC']
data['year'] = data.index.map(lambda x: x.year)
data['date'] = data.index.map(lambda x: x.replace(year=2019))
print(data)
plot = px.line(data, x='date', y='tempC', color='year', line_group='year', error_y='range_max', error_y_minus='range_min')
plot.show()
