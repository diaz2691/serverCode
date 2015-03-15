
import mechanize
#import lxml.html

br = mechanize.Browser()
response = br.open("http://www.apple.com")

for link in br.links():
    print (link.url)
    br.follow_link(link)  # takes EITHER Link instance OR keyword args
    print (br)
    br.back()
