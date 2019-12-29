from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Tools/chromedriver')

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("http://google.com")

driver.find_element_by_name("q").click()
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys("USA")
driver.find_element_by_name(name="btnK").click()

driver.close()
driver.quit()

print("Test done")

