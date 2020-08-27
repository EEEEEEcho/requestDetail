import threading
import time

def start():
    time.sleep(5)
    print(threading.current_thread().name)  # 线程名
    print(threading.current_thread().isAlive()) # 线程是否存活
    print(threading.current_thread().ident)# 线程ID

print('start')
# 注意，这里的参数是方法名，start，而不是start()，加了()就会执行函数，而不是传参，
t =threading.Thread(target=start,name='number one')
t.start()
t.join()    # join()方法，作用是阻塞，等待子线程结束，join方法有一个参数是timeout，即如果主线程等待timeout，
            # 子线程还没有结束，则主线程强制结束子线程。
print('stop')
"""
start
stop
number one
True
12428
"""
# 出现这种情况的原因是，定义的线程为非守护线程，线程的执行并不会随着主线程结束而结束。
