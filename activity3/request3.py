import requests

url = "http://127.0.0.1:5000"

response = requests.post(url + "/weather/Singapore", {})
response = requests.post(url + "/weather/Malaysia", {})
print(response.json())
