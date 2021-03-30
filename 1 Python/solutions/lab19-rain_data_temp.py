




from datetime import datetime


'''
            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
22-DEC-2020     0    0   0   0   0   0   0   0   0   0   0
21-DEC-2020    35    6   7   1   1   0   0   0   1   0   0   0   0   0   0   0   0  12   6   1   0   0   0   0   0
20-DEC-2020   133   11  13  12   4  17   7   5   8   6   7  10   3   7   1   0   0   1   0   1   4   5   5   2   4
'''

# your parsing code here ----

# option 1 - list of dictionaries
data = [{
    'date': datetime(2020, 12, 20),
    'daily_total': 1.33
},{
    'date': datetime(2020, 12, 21),
    'daily_total': 0.35
},{
    'date': datetime(2020, 12, 22),
    'daily_total': 0
}]
# for row in data:
#     print(row['date'])


# option 2 - one big dictionary
data = {
    datetime(2020, 12, 20): 1.33 
}
# for date in data:
#     print(date, data[date])



# option 3 - use a class
class RainDataRow:
    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total
    
    def __str__(self):
        return f'{self.date} {self.daily_total}'

data = [
    RainDataRow(datetime(2020, 12, 20), 1.33),
    ...
]
# for row in data:
#     print(row.date)


# option 4 - use a list of tuples

date_index = 0
data = [(datetime(2020, 12, 20), 1.33), ...]
# for row in data:
#     print(row[date_index])




# import requests
# import time
# start_time = time.time()
# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# end_time = time.time()
# print(response.text)
# print(end_time - start_time, 'seconds')


# relative path
# with open('./data/hayden_island.rain', 'r') as file:
#     text = file.read()

# absolute path
with open(r'C:\Users\flux\programs\class_bumble_bee\1 Python\solutions\data\hayden_island.rain', 'r') as file:
    text = file.read()
print(text)


# use re.findall with capture groups to get the date and daily total




