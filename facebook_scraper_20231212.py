#這是2023.12.12愛交的作業，今2023.12.14補交

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup

path = r'/usr/local/bin/chromedriver'
service=Service(executable_path=path)
chrome=webdriver.Chrome(executable_path=path)
chrome.get('https://mbasic.facebook.com')
time.sleep(5)

un = input("請輸入你的口座：")
pw = input("請輸入你的密碼：")
kw = input("請輸入你欲搜揣的關鍵字：")


un_xpath = '/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[1]/input'
# 讓程式根據xpath找到輸入框
un_element = chrome.find_element(By.XPATH, un_xpath)
un_element.send_keys(un)

pw_xpath='/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[2]/section/input'

pw_element = chrome.find_element(By.XPATH, pw_xpath)
pw_element.send_keys(pw)

login_button_xpath = "/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/form/ul/li[3]/input"
login_button_element = chrome.find_element(By.XPATH, login_button_xpath)
login_button_element.click()

kw_xpath = "/html/body/div/div/div[1]/div/form/table/tbody/tr/td[2]/input"
kw_element = chrome.find_element(By.XPATH, kw_xpath)
kw_element.send_keys(kw)

search_button_xpath = "/html/body/div/div/div[1]/div/form/table/tbody/tr/td[3]/input"
search_button_element = chrome.find_element(By.XPATH, search_button_xpath)
search_button_element.click()

authors = []
for i in range(0, 100):
    try:
        p = chrome.page_source
        soup = BeautifulSoup(p, "lxml")
        p_authors = soup.find_all("h3")
        for aut in p_authors:
            if aut.find("strong")!=None:
                if ">" in aut.text: #檢查有「>」無，若有，表示是社團鋪文               
                    authors.append(aut.text.strip()[0:aut.text.index(">")-1]) #遮會扣1是因為「>」頭前閣有閬一个空，這个空無共strip挕捒尾仔算作者鋪偌濟擺會算做無仝款的作者
                elif "──" in aut.text: #檢查有「──」無，若有，表示有打卡抑是tag其他的人
                    authors.append(aut.text.strip()[0:aut.text.index("──")])
                elif "發佈了" in aut.text: #檢查有「在…發佈了…」無，若有，表示是鋪佇相簿
                    authors.append(aut.text.strip()[0:aut.text.index("在")])
                else:
                    print("作者：", aut.text)
                    authors.append(aut.text)
        time.sleep(0.1)
        chrome.get(soup.find("div", id="see_more_pager").find("a").get("href"))
        print("----第{i}頁----")
    except:
        break
                                                    
#計算作者發文數

aut_count={}

for aut in authors:
    if aut not in aut_count:
        aut_count[aut]=1
    else:
        aut_count[aut]+=1

print(f"「{kw}」的搜揣結果：")
        
for aut in iter(aut_count):
    print(f"{aut}： {aut_count[aut]}篇")