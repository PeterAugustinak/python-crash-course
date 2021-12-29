import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# explore te structure of the data
# for 1 day
# filename = '../data/eq_data_1_day_m1.json'
# for last 30 days
# filename = '../data/eq_data_30_day_m1.json'
# 16-8 current last 24 hours
filename = '../../data/eq_data_24hours.json'

with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

# readable_file = '../data/readable_eq_data.json'
# with open(readable_file, 'w') as f_w:
#     json.dump(all_eq_data, f_w, indent=4)

# 16-7
title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# 16-6
magnitudes = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
longitude = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
latitude = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_title = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

# map the earthquakes
data = [{'type': 'scattergeo',
         'lon': longitude,
         'lat': latitude,
         'text': hover_title,
         'marker': {
             'size': [5*mag for mag in magnitudes],
             'color': magnitudes,
             'colorscale': 'Jet',
             'reversescale': False,
             'colorbar': {'title': 'Magnitude'}
            }
         }]

# 16-7
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,
             filename='../../visualizations/charts/global_earthquakes.html')
