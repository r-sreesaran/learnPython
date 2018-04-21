import json
import urllib.request, urllib.response,urllib.error

url = 'http://jsonplaceholder.typicode.com/comments'
request = urllib.request.urlopen(url).read()

print(request.decode())
first = json.load(request.decode())

print(first[0])