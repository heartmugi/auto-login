from selenium import webdriver
import os
import signal
import re
import config

# Path等の取得
driver_path = config.driver_path
url = config.url
id = config.id
password = config.password
xpaths1 = config.xpaths1
xpaths2 = config.xpaths2
matrix = config.matrix

def main():
    try:
        # ブラウザ立ち上げ
        driver = webdriver.Chrome(driver_path)
        # 指定ページを開く
        driver.get(url)

        # ログイン1
        form = driver.find_element_by_xpath(xpaths1[0])
        form.send_keys(id)
        form = driver.find_element_by_xpath(xpaths1[1])
        form.send_keys(password)
        form.submit()

        # ログイン2
        # 現在ページソースを取得
        source = driver.page_source
        # matrix部分を抽出
        keys = []
        for i in range(len(source)-5):
            s = source[i:i+5]
            if re.search(r'\[[A-Z]+,\d{1}\]', s) is not None:
                keys.append([s[1], int(s[3])])
        # 入力
        for xpath, (k1, k2) in zip(xpaths2, keys):
            form = driver.find_element_by_xpath(xpath)
            form.send_keys(matrix[k1][k2])
        form.submit()

        import time
        time.sleep(5)
        
    finally:
        os.kill(driver.service.process.pid,signal.SIGTERM)

if __name__ == '__main__':
    main()    