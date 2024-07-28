# StringIO操作的只能是str
# 如果要操作二进制数据，就需要使用BytesIO
# ByteIO实现了内存中读写bytes,我们创建一个BytesIO,然后
# 写入一些bytes

from io import BytesIO
f=BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())
