# Socket 是网络编程的一个抽象概念。通常我们用一个
# Socket 表示"打开了一个网络链接"，而打开一个Socket
# 需要知道目标计算机的IP地址和端口号，在指定协议类型即可。

# 导入socket库
import socket

# 创建一个socket:
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCP 连接创建的是双向通道，双方都可以同时给对方发数据。HTTP协议规定客户端必须先发请求
# 给服务器，服务器收到后才能发数据给客户端
# 接收数据：
buffer = []
while True:
    # 每次最多接收1K字节,recv(max)方法，一次最多接收指定的字节数
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接
s.close()
# '\r' 是回车,'\n' 是换行，前者使光标到行首，后者使光标下移一格
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)

