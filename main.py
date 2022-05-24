import requests
import json
url = 'http://localhost:5000/sendMessage'
payload = {'user':"'Ali'",'message':"'hello'"}
for i in range(1000):
    print("Message send")
    r = requests.post(url, data=payload)



r.text
r.status_code