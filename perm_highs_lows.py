import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/perm_weather.csv'
with open(filename) as f:
    #Read a file
    reader = csv.reader(f)
    header_row = next(reader)

    #Data colletion
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f'Missing - {row}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #Data visualization
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

    #Some text
    t = 'Daily temerature high and low for one year\nPerm, Permskiy krai'
    plt.title(t, fontsize=16)
    plt.ylabel('Temperature (C)', fontsize=10)
    fig.autofmt_xdate()

    plt.show()
