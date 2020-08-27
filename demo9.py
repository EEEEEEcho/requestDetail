# post上传文件
import requests

file = {
    'file': ('demo1', open('demo1.py', 'rb'), 'application/html', {'Expires': '0'})
}


def post_html(url):
    html = requests.post(url, files=file)
    if html.status_code == 200:
        html.encoding = "utf8"
        print(html.text)
    else:
        print("get error:" + html.url)


if __name__ == '__main__':
    url = "http://httpbin.org/post"
    post_html(url)
