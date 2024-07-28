# 序列化
# 我们把变量从内存中变成可存储或传输的过程称之为序列化
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化

import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('./dump.txt', 'wb')
# 序列化并写入到文件
pickle.dump(d, f)
f.close()

# Pickle的问题和所有其他编程语言特有的序列化问题一样，
# 就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

f = open('./dump.txt', 'rb')
# 反序列化出一个对象
d = pickle.load(f)
f.close()
print(d)

