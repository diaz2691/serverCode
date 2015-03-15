import urllib.request
from bs4 import BeautifulSoup

site = "http://ilearn.csumb.edu/"

sock = urllib.request.urlopen(site)

htmlSource = sock.read()

sock.close()

soup = BeautifulSoup(htmlSource)

for i in soup('ul' , 'unlist'):
    print (i.text)



