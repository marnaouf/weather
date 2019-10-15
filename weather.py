import pandas as pd
import plotly.express as px

data = pd.read_csv('beirut.csv')

years = []
dates = []
for index, row in data.iterrows():
	date = row['date_time'].split('-')
	years.append(date[0])
	dates.append('-'.join((['2019'] + date[1:])))

data['year'] = years
data['date'] = dates

plot = px.line(data, x='date', y='tempC', color='year', line_group='year', filename='data.html')
plot.show()