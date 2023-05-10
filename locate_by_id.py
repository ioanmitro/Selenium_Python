<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
</html>

# The form element can be located like this
login_form = driver.find_element(By.ID, 'loginForm')

