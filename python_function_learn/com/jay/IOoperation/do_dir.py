import os
#操作系统类型
print(os.name)
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径显示出来
print(os.path.join('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation','testdir'))
# 然后创建一个目录
# print(os.mkdir('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/testdir'))
# 删掉一个目录
# os.rmdir('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/testdir')
# 拆分字符串
print(os.path.split('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/gbk.txt'))
# 得到文件扩展名
print(os.path.splitext('/Volumes/Develop/Python_learn/python_function_learn/com/jay/IOoperation/gbk.txt'))
print(os.rename('gbk.txt','test.py'))
os.remove('test.py')

