# We need to be on the domain that the cookie will be valid for:

# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)

# And output all the available cookies for the current URL
driver.get_cookies()

