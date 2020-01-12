import csv

curatedData = list(csv.reader(open("dataset.csv")))
curatedData.pop(0)

positive = 0
curatedData = sorted(curatedData,key=lambda l:l[8],reverse=True)
for row in curatedData:
    if int(row[8]) == 1:
        positive+=1

with open ('relevancy.txt','w',newline = '') as curated:
    curated.write(str(positive)+"\n")
    for row in curatedData:
        curated.write(row[1]+"\n")
curated.close

curatedData = [row for row in curatedData if int(row[8]) != 0] #Removes data with relevancy of 0

positive = 0
curatedData = sorted(curatedData,key=lambda l:l[6],reverse=True)
for row in curatedData:
    if int(row[6]) == 1:
        positive+=1

with open ('sentiment.txt','w',newline = '') as curated:
    curated.write(str(positive)+"\n")
    for row in curatedData:
        curated.write(row[1]+"\n")
curated.close

positive = 0
curatedData = sorted(curatedData,key=lambda l:l[7],reverse=True)
for row in curatedData:
    if int(row[7]) == 1:
        positive+=1

with open ('technicality.txt','w',newline = '') as curated:
    curated.write(str(positive)+"\n")
    for row in curatedData:
        curated.write(row[1]+"\n")
curated.close