

import re
import requests
from datetime import datetime
import matplotlib.pyplot as plt




# def get_rain_files():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
#     }
#     response = requests.get('https://or.water.usgs.gov/non-usgs/bes/', headers=headers)
#     text = response.text
#     rain_files = re.findall(r'\w+\.rain', text)
#     output = []
#     for rain_file in rain_files:
#         url = 'https://or.water.usgs.gov/non-usgs/bes/' + rain_file
#         name = rain_file.replace('_', ' ').replace('.rain', '').title()
#         output.append({'url': url, 'name': name, 'file_name': rain_file})
#     return output

# def download_all_rain_files():
#     rain_files = get_rain_files()
#     print(f'Downloading {len(rain_files)} files')
#     count = 0
#     for rain_file in rain_files:
#         print('Downloading ' + rain_file['file_name'])
#         response = requests.get(rain_file['url'])
#         text = response.text
#         with open('./data/' + rain_file['file_name'], 'w') as file:
#             file.write(text)
#         count += 1
#         print(str(round(count/len(rain_files)*100,2)) + '%')

# download_all_rain_files()

# def get_rain_data(url):
#     response = requests.get(url)
#     print(response.text)

# rain_files = get_rain_files()
# for i in range(len(rain_files)):
#     print(i+1, rain_files[i]['name'])
# rain_file_index = int(input('Which file would you like to use? '))-1
# get_rain_data(rain_files[rain_file_index]['url'])



# with open('./data/hayden_island.rain', 'r') as file:
#     text = file.read()


# ====== using string methods ======
# lines = text.split('\n')
# lines = lines[11:]
# for line in lines:
#     data = line.split()
#     print(data[0], data[1])



# ====== use a list of tuples ======
# for i in range(len(data)):
#     date = datetime.strptime(data[i][0], '%d-%b-%Y')
#     daily_total = round(int(data[i][1])*0.01*2.54, 4) # daily total in cm
#     data[i] = (date, daily_total)



# ====== using a dictionary with the dates as the keys and the daily totals as the values
# data_dict = {}
# for row in reversed(data):
#     date = datetime.strptime(row[0], '%d-%b-%Y')
#     daily_total = round(int(row[1])*0.01*2.54, 4) # daily total in cm
#     data_dict[date] = daily_total

# average_daily_rainfall = 0
# for date in data_dict:
#     average_daily_rainfall += data_dict[date]
# average_daily_rainfall /= len(data)
# print(average_daily_rainfall)


class RainDataRow:
    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total
    
    def __str__(self):
        return f'{self.date.strftime("%Y/%m/%d")} {self.daily_total}cm'

    def __repr__(self):
        # return str(self)
        return self.__str__()
    
def load_data(path):
    with open(path, 'r') as file:
        text = file.read()
    data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
    # list of class instances
    for i in range(len(data)):
        date = datetime.strptime(data[i][0], '%d-%b-%Y')
        daily_total = round(int(data[i][1])*0.01*2.54, 4) # daily total in cm
        data[i] = RainDataRow(date, daily_total)
    return data

def get_average(data):
    average_daily_rainfall = 0
    for row in data:
        average_daily_rainfall += row.daily_total
    average_daily_rainfall /= len(data)
    return average_daily_rainfall

def get_max_rain(data):
    running_max = data[0]
    for row in data:
        if row.daily_total > running_max.daily_total:
            running_max = row
    return running_max


def plot_all_data(data):
    # x_values = [datetime(2018, 5, 23), datetime(2018, 5, 24)]
    # y_values = [0.56, 1.23]
    x_values = [row.date for row in data]
    y_values = [row.daily_total for row in data]
    plt.plot(x_values, y_values)
    plt.show()


def plot_data_for_year(data, year):
    # x_values = [datetime(2018, 5, 23), datetime(2018, 5, 24)]
    # y_values = [0.56, 1.23]
    x_values = [row.date for row in data if row.date.year == year]
    y_values = [row.daily_total for row in data if row.date.year == year]
    plt.plot(x_values, y_values)
    plt.show()


# get the average rainfall for a given day of the year (e.g. january 1st is 1)
def get_average_for_day(data, day_of_year):
    average = 0
    count = 0
    for row in data:
        if row.date.timetuple().tm_yday == day_of_year:
            average += row.daily_total
            count += 1
    return average / count

def plot_yearly_average(data):
    # x_values = [datetime(2018, 5, 23), datetime(2018, 5, 24)]
    # y_values = [0.56, 1.23]
    x_values = list(range(1, 366)) # day numbers of the year 1-365
    y_values = []
    for day_of_year in x_values: # iterate over our days
        y_values.append(get_average_for_day(data, day_of_year))
    plt.plot(x_values, y_values)
    plt.show()


data = load_data('./data/hayden_island.rain')
average = get_average(data)
max_rain = get_max_rain(data)
print(f'Average: {average}')
print(f'Max rain: {max_rain}')

# plot_all_data(data)
# plot_data_for_year(data, 2005)
plot_yearly_average(data)



