from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)    
click_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
sleep(2)

driver.quit()