"""
使用requests的异步
"""
import asyncio,requests
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.13'
                  '0 Safari/537.36'
}
def crawl(i):
    print("正在执行",i)
    url = "http://xiaohua.zol.com.cn/lengxiaohua/{}.html".format(i)
    html = requests.get(url,headers=headers)
    print(html.status_code)
    soup = BeautifulSoup(html.text,'lxml')
    list = soup.select('.article-list .article-title a')
    for li in list:
        print(li.get_text())


async def main():
    loop = asyncio.get_event_loop()
    tasks = []
    with ThreadPoolExecutor(max_workers=10) as t:
        for i in range(1,10):
            tasks.append(loop.run_in_executor(
                t,
                crawl,
                i
            ))
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()