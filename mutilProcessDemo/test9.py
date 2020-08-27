# 进程通信
# Python多进程之间默认是无法通信的，因为是并发执行的，所以需要借助其他数据结构
# 这里借助队列，一个往队列中写，一个从队列中读，实现消息队列
from multiprocessing import Process,Queue

def write(q):
    print("Process to write : %s" % Process.pid)
    for i in range(100):
        print("Put %d to queue..." % i)
        q.put(i)

def read(q):
    print("Process to read : %s" % Process.pid)
    while True:
        value = q.get()
        print("Get %d from queue." % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传递给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()

