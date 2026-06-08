
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")



wait = WebDriverWait(driver, 30)

time.sleep(5)

try:
    accept_button = wait.until(EC.element_to_be_clickable((By. CSS_SELECTOR, "button.cdx-button--action-progressive")))
    accept_button.click()
    time.sleep(2)

except:
    pass

search_bar = wait.until(EC.element_to_be_clickable((By.ID, "searchInput")))
search_bar.send_keys("Halima Sadiya Danjuma")
search_bar.send_keys(Keys.RETURN)