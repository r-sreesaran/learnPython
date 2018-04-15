#http://py4e-data.dr-chuck.net/known_by_Fikret.html

from bs4 import BeautifulSoup
import urllib.request

url = input('Enter url')
position = int(input('Enter position'))
upto = int(input('Enter count'))
count = 0 


while True:
      if(count > upto-1):
           break
      html = urllib.request.urlopen(url).read()
      soup = BeautifulSoup(html,'html.parser')
      tags = soup('a')
      url = tags[position-1].get('href')
      count = count +1
print(url)
   

    
