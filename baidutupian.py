# coding=utf8
from urllib import parse
from fake_useragent import UserAgent
from uuid import uuid4
import requests
import os

headers = {
    "User-Agent": str(UserAgent().random),
    "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl"
               "=2&lm=-1&st=-1&fr=&sf=1&fmq=1567133149621_R&pv=&ic=0&nc=1&z=0&hd=0&l"
               "atest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype"
               "=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8",
    "Cookie": "BDqhfp=%E5%A3%81%E7%BA%B8%26%2600-10-1undefined%26%268955%26%264; BIDU" \
              "PSID=A9CA40CD7509DCDBCB2358D36CBB2D91; BAIDUID=E0E4E5065F8DB60202662325" \
              "84DB75EE:FG=1; PSTM=1595728572; BDUSS=BwUW5IRjlzcHhLV3E0azBpbkdjTHpGbHhI" \
              "ejFLMG1XanIyY3pJTEVDLXUtVVJmRVFBQUFBJCQAAAAAAAAAAAEAAAB4xj02QWxwYWNhZGF" \
              "oYdi8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK" \
              "5sHV-ubB1ffl; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[xoix5KwSHTc]=" \
              "9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; PSINO=2; H_PS_PSSID=; BDRCVFR[X_XKQks0S" \
              "63]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; fir" \
              "stShowTip=1",
    "Connection": "keep-alive"
}
keyword = parse.quote(input("请输入搜索的图片>>"))
print(keyword)


def download(url):
    filename = "images"
    if not os.path.exists(filename):
        os.makedirs(filename)
    img = requests.get(url, headers=headers)
    with open("./images/{}.jpg".format(uuid4()), "wb") as f:
        f.write(img.content)


def get_json(url):
    json_data = requests.get(url, headers=headers).json()['data']
    for item in json_data[:-1]:
        print(item['middleURL'])
        download(item['middleURL'])


for i in range(30, 300, 30):
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&" \
          "fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&" \
          "st=-1&z=0&ic=0&hd=0&latest=0&copyright=0&word={}&s=&se=&tab=&" \
          "width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&" \
          "pn={}&rn=30&gsm=5a&1595897300035=".format(keyword, keyword, i)
    get_json(url)
