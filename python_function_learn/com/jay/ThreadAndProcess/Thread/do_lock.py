# 多进程和多线程最大的不同之处在于，多进程中，同一个变量，
# 同一个变量各自有一份拷贝存在于每个进程中，
# 同一个变量各自有一份拷贝存在于每个进程中互不影响，而多线程中，所有
# 变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险之处在于多个线程同时改一个变量，把内容给改乱了。

import time, threading

# 假如这是你的银行存款
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完之后一定要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(6,))
t4 = threading.Thread(target=run_thread, args=(7,))
t5 = threading.Thread(target=run_thread, args=(9,))
t6 = threading.Thread(target=run_thread, args=(10,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

print(balance)
