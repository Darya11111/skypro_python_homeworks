from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))


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