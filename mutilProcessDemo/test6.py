# 解决方法，加锁
import threading
lock = threading.Lock()
number = 0
def addNumber():
    global number
    for i in range(1000000):
        lock.acquire()
        number += 1
        lock.release()

def downNumber():
    global number
    for i in range(1000000):
        lock.acquire()
        number -= 1
        lock.release()

print("start")
t = threading.Thread(target=addNumber)
t2 = threading.Thread(target=downNumber)

t.start()
t2.start()
t.join()
t2.join()
print(number)
print("stop")