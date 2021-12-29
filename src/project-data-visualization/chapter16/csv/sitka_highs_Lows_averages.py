import matplotlib.pyplot as plt
import csv
from datetime import datetime


filename = '../../data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temperatures from this file
    dates, highs, lows, averages = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        average = (high + low) / 2
        averages.append(average)

    # highs = [int(row[5]) for row in reader]
    # dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in reader]

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)


# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, averages, c='black')
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)


# format plot
plt.title('Daily high,low and average temperatures, 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()





