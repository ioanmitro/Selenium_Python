from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

deliver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	driver.quit()
# wait for a maximum of 10 seconds for an element matching the given criteria to be found.
# if no element found in that time, TImeoutException is thrown. By default, WebDriverWait calls 
# the ExpectedCondition every 500 milliseconds until it returns success. ExpectedCondition will 
# return true(Boolean) in case of success or not null if it fails to locate an element 
