from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)    
click_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
sleep(2)

driver.quit()