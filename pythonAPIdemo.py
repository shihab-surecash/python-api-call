import requests
import json
import csv


def post_todo():
	api_url = "https://jsonplaceholder.typicode.com/todos"
	reader = csv.DictReader(open("D:/Python API calling/pythonAPIdata.csv"))   

	for row in reader:
	        try:
	        	response = requests.post(api_url, json=row)
	        	response.raise_for_status()

	        except requests.exceptions.RequestException as e:
	        	raise SystemExit(e)	

	        print(response.text)

	        response_time = response.elapsed.total_seconds() * 1000
	        if(response_time > 950):
	        	print ("RESPONSE DELAY !!! response time is " + str(response_time) + " ms which exceeds maximum response time 950 ms")
	        else:
	        	print("response time is " + str(response_time) + " ms which is below maximum response time 950 ms")	
	        

post_todo()


