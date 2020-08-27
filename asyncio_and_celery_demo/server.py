"""
分布式计算思想：
将大人物分散成几个小任务，交给分布式网络中的计算机去完成。
在分布式计算的环境中，必须保证网络中计算机的可用性（避免网络延迟，非预知的崩溃等）。
所以就需要可以可持续的监控框架。
有一个分布式系统基础特征产生的问题：网络由不同操作系统的计算机组成，很多互不兼容。
所以有了兼容不同环境的框架，比如Celery
"""
# 服务端
from celery import Celery
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.13'
                  '0 Safari/537.36'
}
app = Celery(
    'tasks',
    backend='redis://127.0.0.1:6379/0',   # Celery处理完结果后存储到哪里
    broker='redis://127.0.0.1:6379/1'     # broker 消息代理分发器，分发任务
)

# 装饰器，表明这是一个Celery的任务 ,这里只定义了一个任务
@app.task
def get_html():
    print("正在执行")
    url = "http://xiaohua.zol.com.cn/lengxiaohua/1.html"
    html = requests.get(url, headers=headers)
    print(html.status_code)
    soup = BeautifulSoup(html.text, 'lxml')
    list = soup.select('.article-list .article-title a')
    result = ''     #任务返回的结果
    for li in list:
        print(li.get_text())
        result += li.get_text()
    return result