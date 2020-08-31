import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re

headers = {
    'cookie': '_zap=fd55ffed-813b-44e9-abf8-fa1fe5ab6a80; d_c0="AEAXY8d2zRGPTstRnW2CeLF3Hg0Pk48wby0=|1598626230"; '
              '_ga=GA '
              '1.2.1580662395.1598626232; _xsrf=4ecfb6c6-d4dd-44cb-bf72-d276a7c70ad4; '
              'Hm_lvt_98beee57fd2ef70ccdd5ca52b974 '
              '0c49=1598626232,1598627525,1598855008; _gid=GA1.2.2065074380.1598855008; '
              'SESSIONID=84hWfO2DSUbxcnb706hnwUI '
              'HpgrvwYHEbqiBYbdVvSc; JOID=W1AUA0tol3LymnXJXmHvbktWCgxHUaobpfU78hsywxmL'
              '-RKqYD8IP6SSfcFfpWq_nOgFvoZsvDryn9N '
              'cFIiy9cw=; osd=WlsVAE9pnHPxnnTCX2Lrb0BXCQhGWqsYofQw8xg2whKK-haraz4LO6WZfMJbpGG-n-wEtYdvuDv5ntBYFYOz9sg'
              '=; c '
              'apsion_ticket="2|1:0|10:1598855234|14:capsion_ticket|44:YzM1YmFiMjgyOTczNDY2M2IwMjViNDRkMjQ1Yzc1NDI'
              '=|04028 '
              'ce199f4dbb7ca258fe50415bfe1ed1ba3d8a26f86dbc8517316b565e06c"; '
              'KLBRSID=81978cf28cf03c58e07f705c156aa833|159 '
              '8855266|1598855006; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598855268',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 S '
                  'afari/537.36'
}
ids = re.compile('"cardId":"Q_(\d+)', re.S | re.I)
re_content = re.compile('"excerptArea":{"text":"(.*?)"}')

async def get_html():
    url = 'https://www.zhihu.com/billboard'
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            print("知乎热榜状态码,", resp.status)
            text = await resp.text()

    soup = BeautifulSoup(text, 'lxml')
    hotlists = soup.select('.HotList-item')
    for hot in hotlists:
        try:
            title = hot.select_one('.HotList-itemTitle').text
            hot_degree = hot.select_one('.HotList-itemMetrics').text
            print(title, hot_degree)
        except:
            print("Error")
    contents = re_content.findall(text)
    for content in contents:
        print(content)

    hot_ids = ids.findall(text)
    print(hot_ids)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html())
    loop.close()
