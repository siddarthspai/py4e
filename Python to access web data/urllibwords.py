#Program to get wordcount in a webpage using urllib
import urllib.request,urllib.parse,urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    print(line)
    words1=line.decode()
    words=words1.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)