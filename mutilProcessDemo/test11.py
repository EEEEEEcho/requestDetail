# 线程池的包
import time
import threadpool

# 执行较为耗时的函数，需要开启多线程
def get_html(url):
    time.sleep(3)
    print(url)

# 使用多线程执行telnet函数
urls = [i for i in range(10)]
# 建立线程池
pool = threadpool.ThreadPool(10)
# 提交任务给线程池
requests = threadpool.makeRequests(get_html,urls)
# 开始执行任务
for req in requests:
    pool.putRequest(req)
pool.wait()