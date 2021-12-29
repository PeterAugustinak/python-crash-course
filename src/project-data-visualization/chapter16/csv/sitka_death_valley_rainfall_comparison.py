# 16-1
import matplotlib.pyplot as plt
import csv
from datetime import datetime


filename_sitka = '../../data/sitka_weather_2018_simple.csv'
with open(filename_sitka) as f1:
    reader = csv.reader(f1)
    header_row = next(reader)
    # 16-4
    rain_value = header_row[3].upper()

    # get dates and rainfall from this file
    dates, prcps_s = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        dates.append(current_date)
        prcps_s.append(prcp)

    # 16-4
    station_sitka_name = ', '.join(row[1].title().split()[:2])

filename_death_valley = '../../data/death_valley_2018_simple.csv'
with open(filename_death_valley) as f2:
    reader = csv.reader(f2)
    header_row = next(reader)

    # get dates and rainfall from this file
    prcps_dv = []
    for row in reader:
        prcp = float(row[3])
        prcps_dv.append(prcp)

    # 16-4
    station_dv_name = ', '.join(row[1].title().split()[:2])

    # from some reason the death valley file is about 1 record less
    prcps_dv = prcps_dv[:-1]

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps_s, c='blue')
ax.plot(dates, prcps_dv, c='green')

# format plot
title = f'Daily rainfall - {station_sitka_name} vs {station_dv_name}, 2018'
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel(f'{rain_value}', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()





