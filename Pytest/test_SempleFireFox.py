from selenium import webdriver
import pytest

class TestOrange():
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Firefox()  # Optional argument, if not specified will search path.
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self. driver.quit()
        print("Браузер тю тю ")
        print("Браузер тю тю ")


    def test_loging(self,test_setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

    def test_loging1(self,test_setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()




