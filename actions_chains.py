'''
ActionChanis are a way to automate low level interactions such as mouse movements, mouse button actions,
key press, and context menu interactions.
'''

menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(gidden_submenu).perform()

# Actions can also be queud up one by one, then performed:
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
