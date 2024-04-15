from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


for cycle in range(3):
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = "button.btn-primary"
    click_button = driver.find_element(By.CSS_SELECTOR, blue_button).click()
    print(click_button)
    alert_obj = driver.switch_to.alert 
    alert_obj.accept()
    sleep(3)
    driver.refresh()
driver.quit()