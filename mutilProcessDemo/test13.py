# 单线程裸奔执行CPU密集型任务
import concurrent.futures
import time
number_list = [1,2,3,4,5,6,7,8,9,10]

def evaluate_item(x):
    result = count(x)
    return result

def count(number):
    for i in range(0,10000000):
        i+=1
    return number

if __name__ == '__main__':
    # 单线程裸奔
    s1 = time.time()
    for item in number_list:
        print(evaluate_item(item))
    print("单线程裸奔:",time.time() - s1)

    # 多线程，线程池执行
    s2 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item,item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("多线程执行:",time.time() - s2)

    # 多进程，进程池执行
    s3 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("多进程执行:", time.time() - s3)
