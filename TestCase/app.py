import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def driver():
    # Setup
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()

def test_login_and_admin_module(driver):
    # Login
    time.sleep(3)
    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123' + Keys.ENTER)
    time.sleep(3)

    # Verify Login
    assert "dashboard" in driver.current_url, "Login failed"

    # Admin Page
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
    time.sleep(2)

    # Verify Admin Page
    assert "admin/viewSystemUsers" in driver.current_url, "Failed to navigate to Admin Page"
    print("Admin module - System Users test successful.")
