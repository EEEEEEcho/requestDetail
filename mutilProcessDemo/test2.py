import time
import threading

# 多线程执行

def start():
    i = 0
    for i in range(10000000):
        i += 1
    return

def main():
    s = time.time()
    ts = {}
    for i in range(10):
        t = threading.Thread(target=start)
        t.start()
        ts[i] = t       # 线程存储在字典中

    for i in range(10):
        ts[i].join()    # 执行完毕后阻塞

    print(time.time() - s)

if __name__ == '__main__':
    main()

# 造成这种情况的原因就是GIL锁，由于存在这个GIL锁，所以在CPU密集型任务上，消耗的时间反而会更多
# IO密集型则可以达到较好的效果，因为不会用到CPU做很多运算，所以就不会收到GIL锁的干扰
# 要是想更好的解决，就是用多进程，而不是多线程，每个进程都有自己独立的GIL，不会出现进程之间GIL的争抢
# 多进程的创建和销毁开销会很大，成本会更高，而且进程之间无法看到对方的数据，需要使用栈或者队列进行获取，从而提升编程复杂度
