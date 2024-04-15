from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button = 'button[onclick="addElement()"]'
delete_button = 'button.added-manually'

for on_click in range(5):
    
    driver.find_element(By.CSS_SELECTOR, add_button).click()


delete_element = driver.find_elements(By.CSS_SELECTOR, delete_button)
print(len(delete_element))


sleep(5)