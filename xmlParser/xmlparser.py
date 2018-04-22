import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter the url: ')
#url = 'http://py4e-data.dr-chuck.net/comments_87340.xml'

request = urllib.request.urlopen(url).read()
xmlData = ET.fromstring(request)

print('Retrived',len(request),'characters')
count = xmlData.findall('.//count')

sum = 0
for indi in count:
    sum = sum + int(indi.text)
print('sum',sum)