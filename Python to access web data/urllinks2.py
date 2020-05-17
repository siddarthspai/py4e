#Program will use urllib to read the HTML from the data files below, extract the href= values from the 
#anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat 
#the process a number of times, and report the last name you find.
#url is http://py4e-data.dr-chuck.net/known_by_Shelbie.html
#Position is 18 Count is 7
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])
