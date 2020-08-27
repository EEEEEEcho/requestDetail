import multiprocessing
import time
"""
    多进程
"""

def start(i):
    time.sleep(1)
    print(i)
    print(multiprocessing.current_process().name)
    print(multiprocessing.current_process().pid)
    print(multiprocessing.current_process().is_alive())

if __name__ == '__main__':
    print("start")
    p = multiprocessing.Process(target=start,args=(1,),name="Mul process")
    p.start()
    # p.join()
    print("stop")