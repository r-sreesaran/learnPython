from bs4 import BeautifulSoup
import urllib.request

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')

tags = soup('span')

sum = 0 
count = 0 
for tag in tags:
    sum = sum + int(tag.contents[0])
    count = count + 1
print(sum)
print(count)