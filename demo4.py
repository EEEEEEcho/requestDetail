# 获取json数据
import requests

def json_html(url):
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = "utf8"
        for news in html.json():
            print(news['id'],news['title'])
    else:
        print("get error:" + html.url)

if __name__ == '__main__':
    url = "https://news.qq.com/ext2020/apub/json/prevent.new.json"
    json_html(url)