from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\Tools/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_reach_usa(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_name("q").clear()
        self.driver.find_element_by_name("q").send_keys("USA")
        self.driver.find_element_by_name(name="btnK").click()

    def test_reach_trump(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_name("q").clear()
        self.driver.find_element_by_name("q").send_keys("Trump")
        self.driver.find_element_by_name(name="btnK").click()

    def test_reach_london(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_name("q").clear()
        self.driver.find_element_by_name("q").send_keys("London")
        self.driver.find_element_by_name(name="btnK").click()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test done")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestWorkProject2/TestWorkProject/reports'))