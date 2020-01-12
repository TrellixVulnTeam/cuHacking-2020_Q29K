import csv

curatedData = list(csv.reader(open("dataset.csv")))

positive = 0

curatedData.pop(0)

from operator import itemgetter

curatedData.sort(key = itemgetter (8), reverse = True)

with open ('relevancy.txt','w',newline = '') as curated:
 for x in range (len(curatedData)):
     if int(curatedData[x][8]) == 1:
         positive += 1
 curated.write (str(positive) +"\n")
 for x in range (len(curatedData)):
     curated.write(curatedData[x][1] + "\n")

itera = positive - 1
size = len(curatedData) - 1

for x in range (size-itera): 
     curatedData.pop(size - x)

positive = 0

curatedData.sort(key = itemgetter (6), reverse = True)

with open ('sentiment.txt','w',newline = '') as curated:
 for x in range (len(curatedData)):
     if int(curatedData[x][6]) == 1:
         positive += 1
 curated.write (str(positive) +"\n")
 for x in range (len(curatedData)):
     curated.write(curatedData[x][1] + "\n")

curated.close

positive = 0

curatedData.sort(key = itemgetter (7), reverse = True)

with open ('technicality.txt','w',newline = '') as curated:
 for x in range (len(curatedData)):
     if int(curatedData[x][7]) == 1:
         positive += 1
 curated.write (str(positive) +"\n")
 for x in range (len(curatedData)):
     curated.write(curatedData[x][1] + "\n")
curated.close
