from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://facebook.com")

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

email.send_keys("testing@gmail.com")
password.send_keys("testing123")
login = driver.find_element_by_name("login").click()
print('Logged in successfully!!')

time.sleep(5)

AccSettings = driver.find_element(By.CSS_SELECTOR("div[aria-label='Account']")).text
AccSettings.click()
wait = WebDriverWait(driver, 8)
logout = wait.until(expected_conditions.element_to_be_clickable(By.CSS_SELECTOR("i.hu5pjgll.lzf7d6o1.sp_09gpAzWhK7K.sx_2eadd2")).text)
print('Logged out successfully!!')

driver.close()
