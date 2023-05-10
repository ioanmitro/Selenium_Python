from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# create instance of Firefox WebDriver
driver = webdriver.Firefox()
# navigate to a page given by the URL.
driver.get("http://www.python.org")
# assert that title has the word "Python" in it
assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
# send keys similar to entering keys using the keyboard
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# get the result if there is any
assert "No results found." not in driver.page_source
# quit method could also be used instead of close
driver.close()

# selenium webdriver module provides all the WebDriver implementations.
# Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
# The By class is useed to locate elements within a document
