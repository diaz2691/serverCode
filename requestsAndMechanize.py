##over 80 green
##60 to 80 is yellow
##below 60 is red

import requests
import mechanize
##with requests.Session() as c:
##    url = 'https://sso.csumb.edu/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS/'
##    USERNAME = 'diaz2691'
##    PASSWORD = 'Pechocha27!'
##    c.get(url)
#    print (c.get(url))
#    csrftoken = c.cookies['csrftoken']

##    login_data = dict( username = USERNAME, password = PASSWORD, next='/')
##    c.post(url,data=login_data,headers={'Refer': 'https://ilearn.csumb.edu/'})
##    page = c.get('https://ilearn.csumb.edu/my/')
##    print (page.content)

r =requests.get('https://sso.csumb.edu/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS')

print (r.text)

param = {'username':'diaz2691','password':'Pechocha27!'}

r = requests.post("https://sso.csumb.edu/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS/post",params =param)

print (r.url)
print("#######################################")
print(r.text)

nextpage = 'https://ilearn.csumb.edu/my/'

br = mechanize.Browser()

response = br.open(nextpage)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$444444')

print(response)

