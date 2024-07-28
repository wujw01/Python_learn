# TCP是建立可靠连接，并且通信双方都可以以流的
# 形式发送数据，相对于TCP，UDP则是面向无连接的协议
# 数据传输快，但是不可靠，使用UDP协议时，不需要建立连接，
# 只需要知道对方的IP地址和端口号,
# UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP
# 端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999
# 端口可以各自绑定
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据,recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，
    # 直接调用sendto()就可以把数据用UDP发给客户端。
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!' % data, addr)

