import os
'''
fork() 调用一次，返回两次，因为Unix/Linux操作系统自动
把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在
父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID，
'''
print('Process (%s) start..' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process(%s).' % (os.getpid(), pid))
