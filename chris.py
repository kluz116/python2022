import datetime


my_date =  datetime.date(2022,7,1)#datetime.date.today() # if date is 01/01/2018
y,x,z  = my_date.isocalendar()

print(y)
print(x)
print(z)