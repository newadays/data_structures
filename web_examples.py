#urllib
import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError,URLError
# response =urllib.request.urlopen('http://httpbin.org/xml', data=None)


#get
# url = 'http://httpbin.org/get'

# args = {
#     "name": "Gbenga Awodokun",
#     "engineer": True}

# data = urllib.parse.urlencode(args)
# # response = urllib.request.urlopen(url + "?" + data)

# #POST - encode into bytes
# data = data.encode()
# url = "http://httpbin.org/post"

# response = urllib.request.urlopen(url, data = data)
# print(response.status)

# # #--headers
# # print(response.getheaders())

# # #--body
# print(response.read().decode('utf-8'))

#Error handling
# url = "http://httpbin.org/html/thgb"

url = "http://no-such-server.org"

try:
    response = urllib.request.urlopen(url)
    if response.getcode()==HTTPStatus.OK:
        print(response.read().decode('utf-8'))
except HTTPError as err:
    print("Error: {0}".format(err.code))
except URLError as err:
    print("that sucks {0}".format(err.reason))

import requests
from requests import HTTPError, Timeout
from requests.auth import HTTPBasicAuth

# url = "http://httpbin.org/xml"
url = "http://httpbin.org/get"

dataValues = {
    "key1": "value1",
    "key2": "value2"}

# response = requests.get(url, params=dataValues)

# print("status :" , response.status_code)

# print("headers :", response.headers)

# # print("contents :", response.content)

# print("contents as text :", response.text)


# post
url = "http://httpbin.org/delay/5"

# response = requests.post(url, data=dataValues)

# print("status :" , response.status_code)
# print("contents as text :", response.text)

# Custom header to the server
headerValues = {"User-Agent": "Gbenga App / 1.0.0"}

# error handling
# try:

#     response = requests.get(url, headers=headerValues, timeout=2)
#     response.raise_for_status()

#     print("status :" , response.status_code)
#     print("contents as text :", response.text)
# except HTTPError as err:
#     print("Error: {0}".format(err))

# except Timeout as err:
#     print("Request timed out: {0}".format(err))

url = "http://httpbin.org/basic-auth/gbenga/secret"

# myCreds = HTTPBasicAuth("GbengaAwodokun", "MySecretWord")


response = requests.get(url, auth=("gbenga", "secret"))

print(response.status_code)
print(response.text)



#requests
import requests
from requests import HTTPError, Timeout
from requests.auth import HTTPBasicAuth

# url = "http://httpbin.org/xml"
url = "http://httpbin.org/get"

dataValues = {
    "key1": "value1",
    "key2": "value2"}

# response = requests.get(url, params=dataValues)

# print("status :" , response.status_code)

# print("headers :", response.headers)

# # print("contents :", response.content)

# print("contents as text :", response.text)


# post
url = "http://httpbin.org/delay/5"

# response = requests.post(url, data=dataValues)

# print("status :" , response.status_code)
# print("contents as text :", response.text)

# Custom header to the server
headerValues = {"User-Agent": "Gbenga App / 1.0.0"}

# error handling
# try:

#     response = requests.get(url, headers=headerValues, timeout=2)
#     response.raise_for_status()

#     print("status :" , response.status_code)
#     print("contents as text :", response.text)
# except HTTPError as err:
#     print("Error: {0}".format(err))

# except Timeout as err:
#     print("Request timed out: {0}".format(err))

url = "http://httpbin.org/basic-auth/gbenga/secret"

# myCreds = HTTPBasicAuth("GbengaAwodokun", "MySecretWord")


response = requests.get(url, auth=("gbenga", "secret"))

print(response.status_code)
print(response.text)