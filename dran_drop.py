element = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")

from selenium.webdriver import ActionChains
actions_chains = ActionChains(driver)
actions_chains.drag_and_drop(element, target).perform

# moving between named windows using the "switch_to.window" method
driver.switch_to.window("windowName")


# Take a look at the javascript or link that opened it
<a href="somewhere.html" target="windowName">Click here to open a new window</a>

# Alternatively, pass a "window handle" to the "switch_to.window()" method. Knowing this it is possible
# to iterate over every open window like so:
for handle in driver.window_handles:
	driver.switch_to.window(handle)

# We can swing from frame to frame (or into frames):
driver.switch_to.frame("frameName")

# It is possible to access subframes by separating the ptth with a dot, and we can specify the frame
# by its index too. That is:
driver.switch_to.frame("frameName.0.child")

# Come back to parent frame with:
driver.switch_to.default_content()

# To navigate to a page, we use get method:
driver.get("http://www.example.com")

# To move backward and forward in browser's history:
driver.forward()
driver.back()
