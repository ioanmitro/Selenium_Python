class element_has_css_class(object):
	"""An expectation for checking that an element has a particular css class.

	locator - used to find the element.
	returns the WebElement once it has the particular css class.
	"""

	def __init__(self, locator, css_class):
		self.locator = locator
		self.css_class = css_class

	def __call__(self, driver):
		element = driver.find_element(*self.locator) # Finding the referenced element
		if self.css_class in element.get_attribute("class"):
			return element
		else:
			return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'
wait = WebDriveWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))