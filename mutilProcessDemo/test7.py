# 递归锁，为了将锁的粒度控制的更小，更精准，需要使用递归锁
# 缺点：很慢
import time
import threading

class Test:
    rlock = threading.RLock()
    def __init__(self):
        self.number = 0

    def add(self):
        with Test.rlock:    # 这里加了一把锁，执行execute方法，执行后释放
            self.execute(1)

    def down(self):
        with Test.rlock:
            self.execute(-1)

    def execute(self,n):
        # with关键字的使用与打开文件的功能类似，实现自开合效果，
        # 会自动的加锁和释放
        with Test.rlock:    # 这里又加了一把锁，等到执行完加法之后释放
            self.number += n


def add(test):
    for i in range(10000000):
        test.add()

def down(test):
    for i in range(10000000):
        test.down()

if __name__ == '__main__':
    test = Test()
    # args传递方法执行所需要的参数
    t1 = threading.Thread(target=add,args=(test,))
    t2 = threading.Thread(target=down,args=(test,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(test.number)