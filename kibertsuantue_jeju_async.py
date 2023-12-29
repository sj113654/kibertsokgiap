
import time
import requests
from bs4 import BeautifulSoup
import aiohttp, asyncio, json

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

headr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.2'}

async def translate(session, langFrom, langTo, text):
    async with session.get(f'https://lingva.thedaviddelta.com/_next/data/o8We5ZRcFf0mOVj7Hejd6/{langFrom}/{langTo}/{text}.json', headers = headr) as raw:
        if raw.status != 200:
            failedTranslation.append((langFrom, langTo, text))
            return None
        #try:
        tx = json.loads(await raw.text())['pageProps']['translation']
        return tx
        #except Exception:
        #    failedTranslation.append((langFrom, langTo, text))
        #    return None

        
async def bulkTranslate(items):
    async with aiohttp.ClientSession() as sesh:
        tasks = []
        for fromLang, toLang, context in items:
            tasks.append(asyncio.create_task(translate(sesh, fromLang, toLang, context)))
        return await asyncio.gather(*tasks)

news_titles = []
summaries = []
intros = []
poems = []
poets = []
failedTranslation = []
translated_poems = []
world_countries = []

# soup=get_soup("https://ko.wikipedia.org/wiki/대륙별_나라_목록")
# world_countries = soup.find("div", id="mw-content-text").find_all("a")
# for name in world_countries:
#     print(name.text)

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
        text = [('auto', 'zh_HANT', i) for i in poem.split('。') if i]
        translated_poems.append(asyncio.run(bulkTranslate(text)))
        
    news_titles = []
    summaries = []

f = open("詩人統計.html", "w")
f.write("<table border='1'>")
f.write(f"<tr><td>詩人</td><td>詩題</td><td>詩題中譯</td></tr>")

for i in range(len(poets)):
    print("詩人：", poets[i], "詩題：", poems[i], "詩題中譯：", translated_poems[i][0])
    f.write(f"<tr><td>{poets[i]}</td><td>{poems[i]}</td><td>{translated_poems[i][0]}</td></tr>")
    #print("簡介：", intros[i])

f.write("</table>")
f.close()


