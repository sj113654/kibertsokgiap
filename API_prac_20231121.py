
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    try:
        resp=requests.get(url)
        resp.encoding='utf-8'
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'lxml')
            return soup
        else:
            print('網頁取得失敗', resp_status_code)
    except Exception as e:
        print('網址錯誤', e)

resp = get_soup("https://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0")

#由request method=post的header找到參數
api_url = "https://www.ibon.com.tw/retail_inquiry_ajax.aspx"

#組合FormData（互動的參數）
#在payLoad頁籤裡

form_data = {"strTargetField": "COUNTY",
            "strKeyWords": "基隆市"}

#request method不是get，要用post
resp = requests.post(api_url, form_data)

#確定OK後，再用BeautifulSoup來做資料抽取

soup = BeautifulSoup(resp.text, "lxml")

trs = soup.find("table", class_="font16").find_all("tr")

shop_info = []

for i in range(1, len(trs)):
    tds = trs[i].find_all("td")
    shop_info.append([tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip()])
    #tds[0]是店號，tds[1]是店名，tds[2]是住址

df=pd.DataFrame(shop_info, columns = ["店號", "店名", "住址"])

df.to_csv("Kuelâng_shop_info.csv", encoding="utf-8-sig")