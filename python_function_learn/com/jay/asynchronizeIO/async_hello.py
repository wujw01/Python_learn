# asyncio 的编程模型就是一个消息循环，
# 我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行
# 的协程扔到EventLoop中执行，就实现了异步IO。

import threading
import asyncio


# @asyncio.coroutine 把一个generator标记为coroutine类型。
@asyncio.coroutine
def hello():
    print('Hello,world!(%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again!(%s)' % threading.currentThread())


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
