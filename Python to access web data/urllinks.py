#Program to extract all numbers in a webpage and find the sum
#url is http://py4e-data.dr-chuck.net/comments_458409.html
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore ssl cerification errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter: ')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
s=0
#Retrieve all anchor tags
tags=soup('span')
for tag in tags:
    x=tag.contents[0]
    y=int(x)
    s=s+y
print(s)