import requests
from bs4 import BeautifulSoup
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 使用进程池处理大类，使用线程池处理小类
# 以爬取豆瓣图书为例，用进程池处理 各个小说，历史等大类。
# 然后在进程中开线程池去处理分类中的小说

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebK"
                  "it/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Cookie": 'll="108290"; bid=-aVmCi-zzLs; gr_user_id=852f25a0-bb1e-41af-a586-18a3618244be; __yadk_uid=F1bsGV'
              'oTvZDJvpYmLVjhiIsDP1GXbaeb; _vwo_uuid_v2=D667D76296DC6B55BD8CBD126B6447DA2|888b824d46580e1c614e0'
              'd11669878c2; __gads=ID=84ae68a9b581a2b3:T=1597302909:S=ALNI_MZssLhXLwhTf0aHidnY-pjAta5Stw; __utm'
              'a=30149280.1161098309.1597302865.1597302865.1597672767.2; __utmc=30149280; __utmz=30149280.159767'
              '2767.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; gr_session_id_22c937bbd8ebd703f2d8e9445f7d'
              'fd03=dddde28d-ba24-474c-b61c-b1b2521270ef; gr_cs1_dddde28d-ba24-474c-b61c-b1b2521270ef=user_id%3A'
              '0; __utma=81379588.1272962815.1597302909.1597302909.1597672772.2; __utmc=81379588; __utmz=8137958'
              '8.1597672772.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; gr_ses'
              'sion_id_22c937bbd8ebd703f2d8e9445f7dfd03_dddde28d-ba24-474c-b61c-b1b2521270ef=true; _pk_ref.10000'
              '1.3ac3=%5B%22%22%2C%22%22%2C1597672772%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.10000'
              '1.3ac3=*; viewed="25955474_6049132"; __utmt_douban=1; __utmt=1; __utmb=30149280.12.9.1597672767; '
              '__utmb=81379588.10.10.1597672772; _pk_id.100001.3ac3=530267d3dc29ab61.1597302909.2.1597673839.159'
              '7302909.'
}


def get_html(url):
    print("html当前进程{}".format(multiprocessing.current_process().pid))
    html = requests.get(url, headers=headers)
    threadpools = ThreadPoolExecutor(max_workers=3)
    soup = BeautifulSoup(html.text, 'lxml')
    urls = soup.select('.subject-item h2 a')
    for url in urls:
        link = url['href']
        threadpools.submit(get_links, link)


def get_links(url):
    print("获取书的父进程{}".format(multiprocessing.current_process().pid))
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.select_one('#wrapper h1 span').text
    print(title)


if __name__ == '__main__':
    urls = [
        'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',  # 小说
        'https://book.douban.com/tag/%E6%BC%AB%E7%94%BB',  # 漫画
        'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2',  # 历史
    ]
    # get_html(urls[0])
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(get_html, url) for url in urls
        ]
