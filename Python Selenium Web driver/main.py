from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.amazon.com ")

driver.close()
driver.quit()

