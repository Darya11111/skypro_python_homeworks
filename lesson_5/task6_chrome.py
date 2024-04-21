from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")

   
input_username = driver.find_element(By.CSS_SELECTOR, "input#username")
input_username.send_keys("tomsmith")

input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
input_password.send_keys("SuperSecretPassword!")

button_login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(3)

driver.quit()