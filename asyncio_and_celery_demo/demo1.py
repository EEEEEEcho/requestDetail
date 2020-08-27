"""
协程初步：
协程就是一个函数，但是满足以下特征：
1.有I/O依赖的操作，
2.可以在进行I/O操作时暂停，
3.无法直接执行
它的作用就是对有大量I/O操作的程序进行加速
Python协程属于可等待对象，可以在其他协程中被等待。
"""
import asyncio
# async 标记函数是异步函数
async def net():
    return 11

async def main():
    # net() 没办法直接调用
    res = await net()
    print(res)

asyncio.run(main())
