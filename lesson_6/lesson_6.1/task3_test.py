import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(46)
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.get("https://www.saucedemo.com/cart.html")

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Dasha")
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Azeeva")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("620000")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total = driver.find_element(By.CSS_SELECTOR, 'div[data-test="total-label"]').text

    assert total == 'Total: $58.29'

   
    driver.quit()
  