from selenium import webdriver
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome('C:/Tools/chromedriver')  # Optional argument, if not specified will search path.
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()
    print("Браузер тю тю ")
    print("Браузер тю тю ")


def test_loging(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_loging1(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_loging2(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_loging3(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

# def test_tearDown():
#     driver.quit()
#     print("Браузер тю тю ")
#     print("Браузер тю тю ")


