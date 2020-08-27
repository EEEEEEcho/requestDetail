# 使用IP代理
import requests

proxies = {
    "http": "http://118.212.104.230:9999",
    "https": "http://171.35.221.59:9000"
}


def get_url(url):
    html = requests.get(url, proxies=proxies, timeout=3,verify=False)
    if html.status_code == 200:
        print("ok")
    else:
        print("get error:" + url)


if __name__ == '__main__':
    url = "https://kennethreitz.org"
    get_url(url)
