import requests
from _datetime import datetime
import sys
import csv
from datetime import timedelta

url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":"Washington,DC,USA","contentType":"csv","unitGroup":"us","shortColumnNames":"0"}

headers = {
    'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
    'x-rapidapi-key': sys.argv[1]
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

with open('pogoda.csv', 'w', newline="\n") as f:
    writer = csv.writer(f)
    reader = csv.reader(response.text.splitlines(), delimiter=',', quotechar='"')
    for line in reader:
        writer.writerow(line)

sl_pogoda = {}

_date = (datetime.now() + timedelta(days=1)).date()
print(_date.strftime('%m/%d/%Y'))
if len(sys.argv)>2 and sys.argv[2]:
    data = sys.argv[2]
else:
    data = _date.strftime('%m/%d/%Y')

with open('pogoda_history.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        sl_pogoda[line[0]] = line[1]

with open('pogoda.csv') as file:
    reader = csv.reader(file)
    counter = 1
    for linia in reader:
        sl_pogoda[linia[1]] = linia[21]

with open('pogoda_history.csv', 'w') as f:
    writer = csv.writer(f)
    for d, t in sl_pogoda.items():
        writer.writerow([d, t])

for k, v in sl_pogoda.items():
    if v == 'Clear':
        sl_pogoda[k] = 'nie bedzie padac'

for _data in sl_pogoda.keys():
    if _data == data:
        print(sl_pogoda[_data])

print(sl_pogoda)
