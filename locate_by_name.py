<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
 </body>
</html>

# username and password elements can be located like this:
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')


# This will give the "Login" button as it occurs before the "Clear" button
continue = driver.find_element(By.NAME, 'continue')

