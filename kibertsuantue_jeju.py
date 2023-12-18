
import time
import requests
from bs4 import BeautifulSoup

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

def get_translate(chrome, s):
    try:
        chrome.get(f'https://translate.google.com/?sl=ko&tl=zh-TW&text={s}')
        time.sleep(3)

        soup = BeautifulSoup(chrome.page_source, "lxml")
        return soup.find("span", class_="ryNqvb").text
    except Exception as e:
        print(e)
        time.sleep(3)

news_titles = []
summaries = []
intros = []
poems = []
poets = []
translated_poems = []

for page in range(1,10):        
    soup=get_soup(f"https://www.newsnjeju.com/news/articleList.html?page={str(page)}&total=279&sc_word=%EC%95%84%EC%B9%A8%EC%8B%9C&view_type=sm")

    print(f"這馬咧掠第{str(page)}頁")

    for title in soup.find_all(class_="list-dated"):
        if "문학" in title.text:
            news_titles.append(title.find_parent(class_="list-block").find("strong").text)
            summaries.append(title.find_parent(class_="list-block").find("a").text)

    for poet in news_titles:
        if "시인" in poet:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index("시인")]
        elif "작가" in poet:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index("작가")]
        elif "박사" in poet:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index("박사")]
        elif "시인" not in poet:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index("의")]
        elif "(" not in poet:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index(")")]
        else:
            poet = poet.strip("[아침시]")
            poet = poet.strip()[0:poet.index("시인")]
        #print(poet)
        poets.append(poet)

    for poem in news_titles:
        if "'" in poem:
            poem = poem.strip()[poem.index("'")+1:poem.rindex("'")]  
        elif '"' in poem:
            poem = poem.strip()[poem.index('"')+1:poem.rindex('"')]
        if "‘" in poem:
            poem = poem.strip()[poem.index("‘")+1:poem.index("’")]
        elif "“" in poem:
            poem = poem.strip()[poem.index("“")+1:poem.index("”")]
        poems.append(poem)

    news_titles = []
    summaries = []
    
f = open("詩人統計.html", "w")
f.write("<table border='1'>")
f.write(f"<tr><td>詩人</td><td>詩題</td></tr>")

for i in range(len(poets)):
    print("詩人：", poets[i], "詩題：", poems[i])
    f.write(f"<tr><td>{poets[i]}</td><td>{poems[i]}</td></tr>")
    #print("簡介：", intros[i])

f.write("</table>")
f.close()


