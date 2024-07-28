# 1. 从Python3.5 开始引入新的语法 async 和await，可以让
# coroutine 的代码更简洁易读。
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1. 把@asyncioo.coroutine替换为async;
# 2.把yield from 替换为await

# 新
import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()