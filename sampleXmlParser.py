import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')

