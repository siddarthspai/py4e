#Extracting data from XML 
#Total sum of all count tags is found
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url=input('Enter URL:')
if len(url)<1: url="http://py4e-data.dr-chuck.net/comments_458411.xml"
print('Retrieving ',url)

xml = urllib.request.urlopen(url).read()
print('Retrieved: ',len(xml),'characters ')
tree=ET.fromstring(xml)
counts=tree.findall('.//count')
print('Count: ',len(counts))

s=0
for count in counts:
    s+=int(count.text)

print('Sum: ',s)


    