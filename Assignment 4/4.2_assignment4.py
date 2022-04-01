from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.w3schools.com/html/html_lists.asp")

element  = driver.find_element_by_xpath("//*[@class='w3col w3-half']/ol/li[2]").text
print("Single Element: ", element)

li = driver.find_element_by_xpath("//*[@class='w3col w3-half']/ol").text
print("List of elements: ")
print(li)

js = 'alert("Invoked Javacript")'
driver.execute_script(js)
time.sleep(10)
driver.close()