import threading

# 同一线程，同一thread_local
# 不同线程，不同thread_local
# 线程自己的资源，其他线程是无法访问的
a = threading.local()
a.value = "echo"


def change(name):
    try:
        print(threading.current_thread().name, a.value)
    except:
        print(threading.current_thread().name, "No Value")

    a.value = name
    print(threading.current_thread().name, a.value)


for i in range(3):
    threading.Thread(target=change, args=(i,)).start()

print(threading.current_thread().name, a.value)
