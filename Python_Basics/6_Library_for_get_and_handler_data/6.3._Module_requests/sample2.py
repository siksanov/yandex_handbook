from requests import get

param = {'status':'available'}
url = 'https://petstore3.swagger.io/api/v3/pet/findByStatus'
req = get(url, params=param)
print(req.text)