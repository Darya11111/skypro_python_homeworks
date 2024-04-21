from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")
   
input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
input_username.send_keys("tomsmith")

input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
input_password.send_keys("SuperSecretPassword!")

button_login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(3)

driver.quit()