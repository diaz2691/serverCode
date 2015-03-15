##import urllib
##
##username = 'pesq8691'
##password = '0254057W1s13u4kj'
##
###cj = cookielib.CookieJar()
###opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
##login_data = urllib.urlencode({'username' : username, 'j_password' : password})
##opener.open('https://sso.csumb.edu/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS', login_data)
##
##resp = opener.open('/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS')
##print (resp.read())

import mechanize

br = mechanize.Browser()

response = br.open("https://ilearn.csumb.edu/")

for link in br.links():
    print (link.url)


##import mechanize
###import lxml.html
##
##br = mechanize.Browser()
##response = br.open("http://www.apple.com")
##
##for link in br.links():
##    print (link.url)
##    br.follow_link(link)  # takes EITHER Link instance OR keyword args
##    print (br)
##    br.back()
