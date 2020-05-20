#Program to extract data using JSON
#URL is http://py4e-data.dr-chuck.net/comments_458412.json
import json
import urllib.request,urllib.parse,urllib.error

counts = list()
inp = input('Enter a URL:')

url = urllib.request.urlopen(inp)
data = url.read()
print(len(data))

try:
    js = json.loads(data)
except:
    js = None

comments = js['comments']
for comment in comments:
    counts.append(comment['count'])

print(sum(counts))