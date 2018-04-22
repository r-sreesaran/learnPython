import urllib.request,urllib.parse,urllib.response
import json

geoData ='http://py4e-data.dr-chuck.net/geojson?'

location = input('Enter location ')

requestUrl=geoData+urllib.parse.urlencode(
    {'address':location}
)
data = urllib.request.urlopen(requestUrl)
locationDetails=json.load(data)
print(locationDetails['results'][0]['place_id'])
#print(type(locationDetails['results'][0]['place_id']))