import datetime

my_date = datetime.date.today() # if date is 01/01/2018
year, week_num, day_of_week = my_date.isocalendar()

print(f'{week_num} -{year}-{day_of_week}')