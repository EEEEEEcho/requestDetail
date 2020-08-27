import threading
number = 0
def addNumber():
    global number
    for i in range(1000000):
        number += 1

def downNumber():
    global number
    for i in range(1000000):
        number -= 1

print("start")
t = threading.Thread(target=addNumber)
t2 = threading.Thread(target=downNumber)

t.start()
t2.start()
t.join()
t2.join()
print(number)
print("stop")