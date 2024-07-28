f = open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/iotest.txt', 'r')

print(f.read())
f.close()

try:
    f = open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/iotest.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 等同于
with open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/iotest.txt', 'r') as f:
    print(f.read())

# read() 是一次性读取全部内容，如果不能确定文件大小，反复调用
# read(size) 比较保险；如果是配置文件，调用readlines()最为方便
f = open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/iotest.txt', 'r')
for line in f.readline():
    print(line.strip())  # 把末尾的'\n'删掉

# 写文件
f = open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/iotest.txt', 'w')
f.write('xiang.wei 加油')
f.close()

with open('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/gbk.txt','w') as f:
    f.write('你好，世界')


