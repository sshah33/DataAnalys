import csv
import sys
from datetime import datetime

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
file = open('All_Sharepoint_Data.csv')
file2 = open('USCredit_monthly.csv')
reader = csv.reader(file)
reader2 = csv.reader(file2)
daterow = []
dt=next(reader2)
dt.pop(0)
for d in dt:
    daterow.append(datetime.strptime(d, '%m/%d/%Y').date())
print(abs(daterow[1] - daterow[2]))
daterow.pop(0)
#print daterow
next(reader)
for row in reader:
    list = []
    date = datetime.strptime(row[3], '%m/%d/%Y %H:%M').date()
    list.append(row[0])
    list.append(date)
    #list.append(nearest(date, daterow))
    #print list
