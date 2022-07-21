import requests
import json
import csv

api_url = "https://jsonplaceholder.typicode.com/todos"
reader = csv.DictReader(open("D:/Python API calling/pythonAPIdata.csv"))   

for row in reader:
        response = requests.post(api_url, json=row)
        print(response.text)




# with open('D:/Python API calling/pythonAPIdata.csv','rt')as f:
#   data = csv.reader(f)
#   next(data)  #skipping header part of CSV
#   for row in data:
#         response = requests.post(api_url, json=row)
#         print(response)

# parameters = {
#     "lat": 40.71,
#     "lon": -74
# }

# response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)

# print(response.json)

