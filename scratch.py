import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)