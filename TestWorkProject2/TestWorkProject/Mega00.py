import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Tools/chromedriver')  # Optional argument, if not specified will search path.
driver.get("https://mega.ru");
time.sleep(5) # Let the user actually see something!
print("Test done")

driver.quit()







