from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://utexas.campuslabs.com/engage/organizations")

load_more = driver.find_element(By.XPATH, "//div[@class='outlinedButton']")

while True:
    try:
        load_more.click()
        time.sleep(2)
    except:
        break


