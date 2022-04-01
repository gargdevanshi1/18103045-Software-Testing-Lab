from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

#Selecting from dropdown
sel = Select(driver.find_element_by_xpath("//select[@name='continents']"))
time.sleep(5)
sel.select_by_visible_text("Australia")
time.sleep(5)
sel.select_by_index(3)
time.sleep(5)
driver.close()