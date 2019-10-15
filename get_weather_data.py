from wwo_hist import retrieve_hist_data
import pandas as ps
import plotly.express as px

API_KEY = ''
location_list = ['beirut']
start_date = '01-JAN-2009'
end_date = '10-OCT-2019'
freq = 24

data = retrieve_hist_data(API_KEY,
	location_list,
	start_date,
	end_date,
 	freq,
	location_label = False,
	export_csv = True,
	store_df = True)

