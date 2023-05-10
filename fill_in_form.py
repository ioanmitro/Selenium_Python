element = driver.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
	print("Value is: %s" % option.get_attribute("value"))
	option.click()

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

# Webdriver also provides for deselecting all the selected options
select = Select(driver.find_element(By.ID, 'id'))
select.deselect_all()

# This will deselect all OPTIONs from that particular SELECT on the page
# Select class provides a property method that returns a list
select = Select(driver.find_element(By.XPATH, "//select[@name='name']"))
all_selected_options = select.all_selected_options

# Get all available options
options = select.options

# Find the subit button and click it assuming that the button has the ID "submit"
driver.find_element_by_id("submit").click()

# If the element is not in a form, then NoSuchElementException will be raised
element.submit()

