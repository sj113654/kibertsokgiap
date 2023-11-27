import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url, post_data=None):
    try:
        if post_data is not None:
            resp = requests.post(url, post_data, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.2'})
        else:
            resp = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.2'})
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            return soup
        else:
            print('網頁取得失敗', resp.status_code)
    except Exception as e:
        print('網址錯誤', e)

cos = []
api_url = 'https://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs'
table = []

while True:
    co = input('請輸入公司代碼：（按Enter結束）')
    if co == '':
        break
    else:
        cos.append(co)

for stk in cos:
    form_data = {"encodeURIComponent": "1", "step": "1", "firstin": "1", "off": "1", "queryName": "co_id", "inpuType": "co_id", "TYPEK": "all", "isnew": "true", "co_id": stk}
    soup = get_soup(api_url, form_data)
    name = soup.find("td", class_="compName").text
    name = name.strip().strip("本資料由　(上市公司)").strip("　公司提供").strip()
    tds = soup.find("table", class_="hasBorder").find_all("td")
    revenue = tds[0].text.strip()
    percentage_this_month = tds[3].text.strip()
    percentage_accumulate = tds[7].text.strip()
    table.append([stk, name, revenue, percentage_this_month, percentage_accumulate])

df=pd.DataFrame(table, columns=["公司代號", "公司名稱", "本月營收金額", "增減百分比（本月）", "增減百分比（累計）"])
df.to_csv("table.csv", encoding="utf-8-sig")
print(df)