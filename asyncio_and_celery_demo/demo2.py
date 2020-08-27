"""
用睡眠模仿异步I/O函数
"""
import asyncio

async def hello(i):
    print("Hello ", i)
    # 不能使用常规的睡眠机制
    await asyncio.sleep(3)
    print("World ", i)

if __name__ == '__main__':
    tasks = []
    for i in range(4):
        tasks.append(hello(i))
    # 获取事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()