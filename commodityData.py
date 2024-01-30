'''
Program: Commodity data, filtering and visualization
Author: Ashmi Bidrupane Suresh
Purpose: Program to filter and visualization data (replicate)
Revisions: 
    00: To replicate the work
    01: To fix the textgraph 
    02: To add comments
'''
import csv
from datetime import datetime   #import module csv and datetime
with open ('produce_csv.csv','r') as csvfile:   #open and read csv file
    reader = csv.reader(csvfile)
    data = [row for row in reader]
modData = []   #initialize new list to receive data
for row in data:   #traverse the rows
    newRow = list()   #make an empty row to receive values
    for item in row:   #traverse the values in the old row
        if "$" in item:   #test for price string and convert
            newRow.append(float(item.replace("$","")))
        elif "/" in item:   #test for date and convert
            newRow.append(datetime.strptime(item,'%m/%d/%Y'))
        else:   #otherwise append item (not a date or a price)
            newRow.append(item)
    modData.append(newRow)
locations = modData.pop(0)[2:]   #remove header and slice
records = list()   #create empty list for data records
for row in modData:   #traverse each row
    newRow = row[:2]   #first two values are common for all five locations
    for loc, price in zip(locations,row[2:]):   #traverse locations and prices
        records.append(newRow+[loc,price])   #add a new data record

select = list(filter(lambda x: x[0]=='Oranges' and x[2]=='Chicago',records))   
   #use filter function to create a list containing prices recorded 
   #for the retail sale of Oranges in Chicago across all avail. dates
dates = [x[1] for x in select]   #collect the dates for Oranges in Chicago
prices = [x[3] for x in select]   #collect the prices for Oranges in Chicago
dpMerge = [ [d,p] for d,p in zip(dates,prices) ]   #merge the two lists
dpMerge.sort(key=lambda a: a[0])   #sort the merged list by date

for x in dpMerge:   #create and fix the textgraph
    print(f'{datetime.strftime(x[0],"%m-%d-%Y")} {int(25*x[1])*"="}')
    
import matplotlib.pyplot as plt   #import modules for visualization
import matplotlib.ticker as mtick

fig = plt.figure()   #create a figure, returns a figure object
ax = fig.add_subplot()   #add an axis object to the figure
ax.plot(dates,prices,label="Oranges in Chicago")   #add the data series
ax.set_xlabel('date')   #a title for the x-axis
ax.set_ylabel('price in dollars')   #a title for the y-axis
fmt = '${x:,.2f}'   #format for dollars w/ 2 decimal places
tick = mtick.StrMethodFormatter(fmt)   #define the format
ax.yaxis.set_major_formatter(tick)   #establish format for y-axis labels
plt.legend()   #add a legend
plt.show()   #show the figures




    
