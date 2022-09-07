import xml.etree.ElementTree as ET
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_1547489.xml'
response = urllib.request.urlopen(url).read()
tree = ET.fromstring(response)

r = 0

for i in tree:
    for n in i:
        f = int(n.find('count').text)
        r += f
#s
print(r)