import asyncio
import aiohttp
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.13'
                  '0 Safari/537.36'
}


# http://xiaohua.zol.com.cn/lengxiaohua/
async def crawl(i):
    url = "http://xiaohua.zol.com.cn/lengxiaohua/{}.html".format(str(i))
    print("正在爬取。。。", i)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            print(resp.status)
            text = await resp.text()

    soup = BeautifulSoup(text, 'lxml')
    list = soup.select('.article-list .article-title a')
    for li in list:
        print(li.get_text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [crawl(i) for i in range(1, 10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
