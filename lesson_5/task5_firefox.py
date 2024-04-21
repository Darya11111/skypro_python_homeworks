from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
sleep(2)
input_field.send_keys("1000")
sleep(2)
input_field.clear()
input_field.send_keys("999")
sleep(2)

driver.quit()
