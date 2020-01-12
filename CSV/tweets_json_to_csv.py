import json
import os
import csv

tweetsDict = ""

with open ('tweets.json','r', errors='ignore') as oldJson:
    data = oldJson.read().replace('\\n', '')
    with open('temp.json', 'w') as newJson:
        newJson.write(data)
    newJson.close()
oldJson.close()

with open ('temp.json','r', errors='ignore') as tweetsJson:

 tweetsDict = json.load(tweetsJson)

 isHeader = 0
 isFirst = 0
tweetsJson.close()

with open ('dataset.csv','a', newline = '') as data:
 tweetsDict[0]["positive"] = ''
 tweetsDict[0]["tech"] = ''
 tweetsDict[0]["bank"] = ''

 if (isHeader == 0):

     wrt = csv.DictWriter(data,fieldnames = tweetsDict[0].keys())
     if isFirst == 0:
         wrt.writeheader()
     isHeader = 1

 wrt.writerows(tweetsDict)
data.close()

os.remove("tweets.json")
os.remove("temp.json")