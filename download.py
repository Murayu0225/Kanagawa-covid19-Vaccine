from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions, Remote
# 待機に必要
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": "/home/yamada/public_html/download"
})
# prefs オプションを設定、デフォルトのダウンロードディレクトリ変更
driver = webdriver.Chrome(options=options)
time.sleep(1) # 秒 なくても動いた念のため
driver.get("https://www.pref.kanagawa.jp/docs/ga4/covid19/vaccine.html")
# CSVファイルのサンプルダウンロードサイト
driver.find_element_by_partial_link_text(u"こちら（CSV：3KB）（別ウィンドウで開きます）").click()
time.sleep(5) # 秒
driver.quit()
# ブラウザーを終了する。
