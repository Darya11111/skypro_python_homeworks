import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    zip_code_red_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")    
    assert zip_code_red_color == 'rgba(248, 215, 218, 1)'

    other_input_fields = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#job-position", "#company"]
    for field in other_input_fields:
        green_color = driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
        #return(green_color)
        assert green_color == 'rgba(209, 231, 221, 1)'
    driver.quit()




