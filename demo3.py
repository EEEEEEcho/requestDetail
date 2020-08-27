# post发送表单
import requests


def post_html(url):
    data = {"name": "python", "pwd": "123"}
    html = requests.post(url, data=data)
    if html.status_code == 200:
        html.encoding = "utf8"
        print(html.text)
    else:
        print("get error:" + html.url)


if __name__ == '__main__':
    url = "http://httpbin.org/post"
    post_html(url)
