from selenium import webdriver
from selenium.webdriver.support.ui import Select # for <SELECT> HTML form

driver = webdriver.PhantomJS('C:\phantomjs\phantomjs.exe')
# On Windows, use: webdriver.PhantomJS('C:\phantomjs-1.9.7-windows\phantomjs.exe')

# Service selection
# Here I had to select my school among others 
driver.get("https://sso.csumb.edu/cas/login?service=http%3A%2F%2Filearn.csumb.edu%2Flogin%2Findex.php%3FauthCAS%3DCAS")

# Login page (https://cas.ensicaen.fr/cas/login?service=https%3A%2F%2Fshibboleth.ensicaen.fr%2Fidp%2FAuthn%2FRemoteUser)
# Fill the login form and submit it
driver.find_element_by_id('username').send_keys("")
driver.find_element_by_id('password').send_keys("")
driver.find_element_by_id('fm1').submit()

# Now connected to the home page
# Click on 3 links in order to reach the page I want to scrape

# Select and print an interesting element by its ID
page = driver.find_element_by_class_name('logininfo')
print (page.text)
