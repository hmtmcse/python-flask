import requests


response = requests.get('http://localhost:8088/')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.get('http://localhost:8088/request-methods')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.post('http://localhost:8088/request-methods')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.patch('http://localhost:8088/request-methods')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.delete('http://localhost:8088/request-methods')
print("Code: " + str(response.status_code) + " Body: " + response.text)


response = requests.post('http://localhost:8088/json-data', json= {'username': 'Touhid', 'password': '123456'})
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.post('http://localhost:8088/json-data-to-json', json= {'username': 'Touhid', 'password': '123456'})
print("Code: " + str(response.status_code) + " Body: " + response.text)


response = requests.post('http://localhost:8088/thread-ex1')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.post('http://localhost:8088/thread-ex1')
print("Code: " + str(response.status_code) + " Body: " + response.text)

response = requests.post('http://localhost:8088/thread-ex1')
print("Code: " + str(response.status_code) + " Body: " + response.text)