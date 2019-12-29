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
        driver = self.driver
        driver.get("https://mega.ru/belaya_dacha/")
        driver.find_element_by_name("query").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Поиск'])[1]//*[name()='svg'][1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Поиск'])[1]//*[name()='svg'][1]").send_keys(
            "акции")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Поиск'])[2]//*[name()='svg'][1]").click()


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test done")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/karmazin/Documents/GitHub/TestWorkProject/reports'))