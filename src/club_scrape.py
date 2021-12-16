from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://utexas.campuslabs.com/engage/organizations")

load_more = driver.find_element(By.XPATH, "//div[@class='outlinedButton']")

# scrolls to all ~800 results
# while True:
#     try:
#         load_more.click()
#         time.sleep(2)
#     except:
#         break

cards = driver.find_elements(By.XPATH, "//div[@class='MuiPaper-root MuiCard-root MuiPaper-elevation3 MuiPaper-rounded']")

for card in cards:
    print(card.find_element(By.XPATH, "//span//div//div").text)
    print(card.find_element(By.XPATH, "//p[@class='DescriptionExcerpt']").text)

driver.quit()
