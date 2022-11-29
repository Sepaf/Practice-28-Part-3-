#Python -m pytest -v --driver Chrome --driver-path C:/Python2/pythonProject2222/chromedriver.exetest_key.py

import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import Name, valid_email, valid_password, The_code, Mobile_phone, Symbols_from_the_picture

@pytest.fixture(autouse=True)
def Keyy():
    driver = webdriver.Chrome('/pythonProject2222/chromedriver.exe')
    # Переходим на стартовую страницу
    driver.get('https://key.rt.ru')
    yield driver
    driver.quit()

# Авторизация по мобильному телефону
def test_Key1(Keyy):
   driver = Keyy
   # Переходим на страницу авторизации.
   driver.get('https://key.rt.ru')
   time.sleep(10)
   driver.find_element(By.CLASS_NAME, 'go_kab').click()
   time.sleep(5)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(5)
   driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('K1.png')


# Авторизация по электронной почте
def test_Key2(Keyy):
   driver = Keyy
   # Переходим на страницу авторизации.
   driver.get('https://key.rt.ru')
   time.sleep(10)
   driver.find_element(By.CLASS_NAME, 'go_kab').click()
   time.sleep(5)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(5)
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   time.sleep(5)
   driver.find_element(By.ID, 'username').send_keys(valid_email)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('K2.png')


# Авторизация по логину
def test_Key3(Keyy):
   driver = Keyy
   # Переходим на страницу авторизации.
   driver.get('https://key.rt.ru')
   time.sleep(10)
   driver.find_element(By.CLASS_NAME, 'go_kab').click()
   time.sleep(5)
   driver.find_element(By.ID, 'standard_auth_btn').click()
   time.sleep(5)
   driver.find_element(By.ID, 't-btn-tab-login').click()
   time.sleep(5)
   driver.find_element(By.ID, 'username').send_keys(Name)
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(3)
   driver.save_screenshot('K3.png')

# Авторизация по мобильному телефону с кодом
def test_Key4(Keyy):
   driver = Keyy
   # Переходим на страницу авторизации.
   driver.get('https://key.rt.ru')
   time.sleep(10)
   driver.find_element(By.CLASS_NAME, 'go_kab').click()
   time.sleep(5)
   driver.find_element(By.ID, 'address').send_keys(Mobile_phone)
   driver.find_element(By.ID, 'captcha').send_keys(Symbols_from_the_picture)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   driver.save_screenshot('K4.png')

# Авторизация по электронной почте с кодом
def test_Key5(Keyy):
   driver = Keyy
   # Переходим на страницу авторизации.
   driver.get('https://key.rt.ru')
   time.sleep(10)
   driver.find_element(By.CLASS_NAME, 'go_kab').click()
   time.sleep(5)
   driver.find_element(By.ID, 'address').send_keys(valid_email)
   driver.find_element(By.ID, 'captcha').send_keys(Symbols_from_the_picture)
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   driver.save_screenshot('K5.png')
