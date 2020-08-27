import requests

def get_html(url):
    # 这个传入的参数是拼接在url中的一组参数
    param = {"wd": "c++"}
    html = requests.get(url,params=param)
    if html.status_code == 200:
        html.encoding="utf8"
        print(html.text)
    else:
        print("ERROR",html)
if __name__ == '__main__':
    url = "http://www.baidu.com/s"
    get_html(url)