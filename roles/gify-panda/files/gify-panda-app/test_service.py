import requests

status = requests.get('http://localhost:8080/gify').status_code
if status != 200:
    raise Exception('wrong response')
else:
    print('Correct response')
