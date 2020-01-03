from selenium import webdriver
import pytest


# Fixture for Chrome
@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    print("Browser closed")

@pytest.mark.usefixtures("driver_init")
class TestOrange():

    def test_loging(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    def test_google(self):
        self.driver.get("https://www.google.com/")

    def test_google1(self):
        self.driver.get("https://www.google.com/")

    def test_google2(self):
        self.driver.get("https://www.google.com/")

    def test_google3(self):
        self.driver.get("https://www.google.com/")

    def test_google4(self):
        self.driver.get("https://www.google.com/")







    # def test_loging1(self):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_id("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_id("btnLogin").click()




