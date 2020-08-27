# 忽略https证书验证
import requests

def get_url(url):
    html = requests.get(url,verify=False)
    if html.status_code == 200:
        print("OK")
    else:
        print("Error:" + url)

if __name__ == '__main__':
    url = "https://kennethreitz.org"
    get_url(url)