# 进程池

import multiprocessing

def function_square(data):
    result = data * data
    return result

if __name__ == '__main__':
    inputs = list(range(100))
    pool = multiprocessing.Pool(processes=4) # 大小为4
    # map把任务交给进程池处理
    pool_outputs = pool.map(function_square,inputs)
    # apply每次提交一个任务
    # pool_outputs = pool.map(function_square,args=(10,))
    pool.close()
    pool.join()
    print("Pool    :",pool_outputs)
