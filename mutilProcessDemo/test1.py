import time
# 单线程裸奔
def start():
    i = 0
    for i in range(10000000):
        i += 1
    return

def main():
    s = time.time()
    for i in range(10):
        start()
    print(time.time() - s)

if __name__ == '__main__':
    main()