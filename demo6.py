# 使用session维持会话，减少频繁发起请求
import requests
from uuid import uuid4
# 图片下载
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&"
               "st=-1&fr=&sf=1&fmq=1567133149621_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se"
               "=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8",
    "Cookie": "BIDUPSID=A9CA40CD7509DCDBCB2358D36CBB2D91; BAIDUID=E0E4E5065F8DB6020266232584DB75EE:FG=1;"
              " PSTM=1595728572; BDUSS=BwUW5IRjlzcHhLV3E0azBpbkdjTHpGbHhIejFLMG1XanIyY3pJTEVDLXUtVVJmRVF"
              "BQUFBJCQAAAAAAAAAAAEAAAB4xj02QWxwYWNhZGFoYdi8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
              "AAAAAAAAAAAAAAAAAAAAAAAAAK5sHV-ubB1ffl; BDRCVFR[xoix5KwSHTc]=9xWipS8B-FspA7EnHc1QhPEUf; de"
              "lPer=0; PSINO=2; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[X_XKQks0S63]"
              "=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1"
}

session = requests.session()
session.headers = headers

def post_url(url):
    html = session.get(url)
    if html.status_code == 200:
        html.encoding = "utf8"
        content = html.json()['data']
        # print(content)
        for item in content:
            if len(item) > 0:
                download(item['middleURL'])


def download(url):
    img = session.get(url)
    print("正在下载{}".format(url))
    with open("./images/{}.jpg".format(uuid4()), 'wb') as f:
        # 每次下载225字节
        for chunk in img.iter_content(225):
            f.write(chunk)


if __name__ == '__main__':
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&hd=0&latest=0&copyright=0&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn=30&rn=30&gsm=1e&1595855122224="
    post_url(url)
