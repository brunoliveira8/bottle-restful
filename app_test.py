import requests, json

r = requests.get('http://localhost:8080/task/1')

print r.json()