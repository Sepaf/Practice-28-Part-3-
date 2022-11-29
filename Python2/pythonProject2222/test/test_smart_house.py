#Python -m pytest -v --driver Chrome --driver-path C:/Python2/pythonProject2222/chromedriver.exetest_smart_house.py

import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import Name, valid_email, valid_password, The_code, Mobile_phone

@pytest.fixture(autouse=True)
def house():
    driver = webdriver.Chrome('/pythonProject2222/chromedriver.exe')
    # Переходим на стартовую страницу
    driver.get('https://lk.smarthome.rt.ru')
    yield driver
    driver.quit()

# Авторизация по мобильному телефону
def test_smart_house1(house):
   driver = house
   # Переходим на страницу авторизации.
   driver.get('https://lk.smarthome.rt.ru')
   time.sleep(10)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(10)
   driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('R1.png')

# Авторизация по электронной почте
def test_smart_house2(house):
   driver = house
   # Переходим на страницу авторизации.
   driver.get('https://lk.smarthome.rt.ru')
   time.sleep(10)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(10)
   driver.find_element(By.ID, 'username').send_keys(valid_email)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('R2.png')


# Авторизация по логину
def test_smart_house3(house):
   driver = house
   # Переходим на страницу авторизации.
   driver.get('https://lk.smarthome.rt.ru')
   time.sleep(10)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(10)
   driver.find_element(By.ID, 'username').send_keys(Name)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('R3.png')


# Авторизация по мобильному телефону с однаразовым кодом
def test_smart_house4(house):
   driver = house
   # Переходим на страницу авторизации.
   driver.get('https://lk.smarthome.rt.ru')
   time.sleep(10)
   driver.find_element(By.ID, 'address').send_keys(Mobile_phone)
   driver.find_element(By.ID, 'captcha').send_keys(The_code)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('R4.png')
