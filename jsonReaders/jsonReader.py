import urllib.request,urllib.parse,urllib.error
import json

url = input('Enter the url ')
data = urllib.request.urlopen(url)
jsonData = json.load(data)

comments = jsonData['comments']   
dict = 0
for item in comments:
    dict = dict + int(item['count'])

print(dict)