#Python -m pytest -v --driver Chrome --driver-path C:/Python2/pythonProject2222/chromedriver.exetest_oline_web.py

import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import Name, valid_email, valid_password, The_code, Mobile_phone

@pytest.fixture(autouse=True)
def autrz():
    driver = webdriver.Chrome('/pythonProject2222/chromedriver.exe')
    # Переходим на стартовую страницу
    driver.get('https://my.rt.ru')
    yield driver
    driver.quit()

# Авторизация по мобильному телефону
def test_autr1(autrz):
    driver = autrz
    # Переходим на страницу авторизации.
    driver.get('https://my.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    time.sleep(10)
    driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    driver.save_screenshot('RESALT1.png')

# Авторизация по электронной почте
def test_autr2(autrz):
    driver = autrz
    # Переходим на страницу авторизации.
    driver.get('https://my.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    driver.save_screenshot('RESALT2.png')

# Авторизация по логину
def test_autr3(autrz):
    driver = autrz
    # Переходим на страницу авторизации.
    driver.get('https://my.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'standard_auth_btn').click()
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(Name)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    driver.save_screenshot('RESALT3.png')

# Авторизация по мобильному телефону c использованием одноразового кода
def test_autr4(autrz):
    driver = autrz
    # Переходим на страницу авторизации.
    driver.get('https://my.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'address').send_keys(Mobile_phone)
    driver.find_element(By.ID, 'captcha').send_keys(The_code)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    driver.save_screenshot('RESALT4.png')

# Авторизация по электронной почте  c использованием одноразового кода
def test_autr5(autrz):
    driver = autrz
    # Переходим на страницу авторизации.
    driver.get('https://my.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'address').send_keys(valid_email)
    driver.find_element(By.ID, 'captcha').send_keys(The_code)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    driver.save_screenshot('RESALT5.png')