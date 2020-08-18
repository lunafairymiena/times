#!/usr/bin/env python
# coding: utf-8

# In[1]:


# coding: utf-8
# seleniumをインストールする
#Microsoft Windows [Version 10.0.18363.900]
#(c) 2019 Microsoft Corporation. All rights reserved.
#
#C:\WINDOWS\system32>pip install selenium
#Collecting selenium
#  Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
#     |████████████████████████████████| 904 kB 939 kB/s
#Requirement already satisfied: urllib3 in c:\users\user\anaconda3\lib\site-packages (from selenium) (1.25.8)
#Installing collected packages: selenium
#Successfully installed selenium-3.141.0
#
#C:\WINDOWS\system32>


# In[2]:


# https://sites.google.com/a/chromium.org/chromedriver/downloads からchromedriverをインストール
# その前にchromeダウンロードしていなかった。
# ダウンロード実施
# バージョン: 84.0.4147.105（Official Build） （64 ビット）

# If you are using Chrome version 84, please download ChromeDriver 84.0.4147.30

# https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_win32.zip をダウンロード
#    32って書いてあるけどいいのかな。64は無い。とりあえず

# システムパスのフォルダに入れろ、と言われたので　"C:\Windows\System32\chromedriver.exe" にコピー


# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
import locale
import csv

locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")

dt_now = datetime.datetime.now()
dt_str = dt_now.strftime("%Y/%m/%d %H:%M:%S")
fn_str = dt_now.strftime("data%Y%m%d%H%M%S.csv")

options = Options()
options.add_argument('--headless')
# driver = webdriver.Chrome(driver_path)
driver = webdriver.Chrome('C:\windows\system32\chromedriver',options=options)
driver.get("https://times-info.net/P23-aichi/C106/") # 名古屋市中区
#driver.get("https://times-info.net/P23-aichi/C204/") # 瀬戸市
sleep(3)

cnt = 1
cnt2 = 1
tocnt = int(driver.find_element_by_id('pToCount').text)
allcnt = int(driver.find_element_by_id('pAllCount').text)
    
elem_page = driver.find_elements_by_xpath('/html/body/main/section/section[2]/div[1]/div[2]/div[1]/div[1]/ul//a')

with open(fn_str, 'w' , encoding="utf-8",newline="") as f:
    writer = csv.writer(f)

    for elem_h3 in driver.find_elements_by_xpath('//article/a/div/div[1]/div[2]/div[1]'):
        elem_a = elem_h3.find_element_by_xpath('../../div[1]') 
#        print(cnt2, ' ' , elem_h3.text,' ' ,elem_a.text,' ',dt_str)
        writer.writerow([cnt2,elem_h3.text,elem_a.text,dt_str])
        cnt2 += 1
        if cnt2 > tocnt:
            if cnt2 > allcnt:
                break
            elem_page2 = elem_page[cnt]
            elem_page2.click()
            sleep(3)
            tocnt = int(driver.find_element_by_id('pToCount').text)
            cnt += 1
        
driver.close()
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



