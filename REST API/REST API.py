import requests
import json
#GET
res = requests.get('http://222.98.63.219')
# print(str(res.status_code)+'|'+res.text)

#POST
# headers = {'Content-Type':'application/json; chearset = utf-8'}
# data = {'title':'dummy title', 'id': 1, 'message':'hello world!'}
# res = requests.post('http://222.98.63.219', data=json.dumps(data), headers = headers)
# print(str(res.status_code)+"|"+res.text)

from urllib import request, parse
import json

#GET
req = request.Request('http://222.98.63.219')
res = request.urlopen(req)
print(str(res.status)+"|"+res.read().decode('utf-8'))

