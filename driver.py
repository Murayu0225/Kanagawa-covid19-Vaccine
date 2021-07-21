import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


options =  Options();
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=os.getcwd() +"/chromedriver", options=options)
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
