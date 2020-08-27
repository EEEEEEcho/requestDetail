# 守护线程，会伴随主线程一起结束
# setDaemon设置为True即可，但是如果守护线程使用了 join方法，还是会等线程执行完毕，再执行主线程
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
t.setDaemon(True)       # 设置为守护线程，主线程结束，守护线程无论执行完毕与否，都会结束
t.start()
print('stop')