import csv
from datetime import datetime

from plotly.graph_objs import Layout
from plotly import offline


filename = '../data/fires_24h_world.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and rainfall from this file
    lats, longs, brights, dates, times = [], [], [], [], []
    for row in reader:
        lat = row[0]
        long = row[1]
        bright = float(row[2])
        date = row[5]
        time = row[6]
        lats.append(lat)
        longs.append(long)
        brights.append(bright)
        dates.append(date)
        times.append(time)

# making nicely formatted date with time for hover
date_time = [datetime.strptime(f'{date}, {time}', '%Y-%m-%d, %H%M') for
             date, time in zip(dates, times)]


def brightness(br):
    """Differentiate brightness more"""
    br = br / 150
    return br * br * br


# map the earthquakes
data = [{'type': 'scattergeo',
         'lon': longs,
         'lat': lats,
         'text': date_time,
         'marker': {
             'size': list(map(brightness, brights)),
             'color': brights,
             'colorscale': 'Reds',
             'reversescale': False,
             'colorbar': {'title': 'Fire Power'}
            }
         }]

# 16-7
my_layout = Layout(title='Fires burning in last 24 hours')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='graphs/global_fires_24h.html')
