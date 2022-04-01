from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://facebook.com")

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

email.send_keys("incorrect@gmail.com")
password.send_keys("testing123")
login = driver.find_element_by_name("login").click()
print('Incorrect Credentials!!')

driver.close()