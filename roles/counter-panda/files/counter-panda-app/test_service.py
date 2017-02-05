import requests

start = requests.get('http://localhost:8080/counter').text
requests.post('http://localhost:8080/counter')
requests.post('http://localhost:8080/counter')
end = requests.get('http://localhost:8080/counter').text
diff = int(end) - int(start)
if diff != 2:
    raise Exception('wrong response')
