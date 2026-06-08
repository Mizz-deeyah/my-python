from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


#Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_page")

#Hone in anchor tag using CSS selectors
# article_count= driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

#Find the " search" <input> by Name
search = driver.find_element(By.NAME, value="search")

#Sending Keyboard input to Selenium
search.send_keys("python", Keys.ENTER)
