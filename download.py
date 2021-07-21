from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions, Remote
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("prefs", {
  "download.default_directory": "Data/"
})
driver = webdriver.Chrome(options=options)
time.sleep(1)
driver.get("https://www.pref.kanagawa.jp/docs/ga4/covid19/vaccine.html")
driver.find_element_by_partial_link_text(u"こちら（CSV：3KB）（別ウィンドウで開きます）").click()
time.sleep(5)
driver.quit()
