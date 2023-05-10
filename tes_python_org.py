import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

# setUp method will get called before every test function that is going to be written
	def setUp(self):
		self.driver = webdriver.Firefox()

# creates a local reference to the driver object created in setUp method
	def test_search_in_python_org(self):
		driver = self.driver
# navigate to a page given by the URL
		driver.get("http://www.python.org")
# confirm that title has the word "Python" in it
		self.assertIn("Python", driver.title)
		myelem = driver.find_element(By.NAME, "q")
		myelem.send_keys("pycon")
		myelem.send_keys(Keys.RETURN)
# assert whether results were found or not
		self.assertNotIn("No serach results.", driver.page_source)

# tearDown method will get called after every test method. It is a place to do all cleanup actions.
	def tearDown(self):
# close method to close the tab if opened(exit browser)
		self.driver.close()

if __name__ == "__main__":
# run test suite
	unittest.main()