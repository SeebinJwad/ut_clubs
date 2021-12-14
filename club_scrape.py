from selenium import webdriver

driver = webdriver.Chrome()

driver.get("utexas.campuslab.com/engage/organizations")

driver.execute_script("window.scrollTo(0, Y)")



