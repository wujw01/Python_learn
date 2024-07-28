from collections import namedtuple

# namedtuple是一个函数，它用来创建一个自定义的tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# 使用list存储数据时，按索引访问元素很快，
# 但是插入和删除元素就很慢了,
# deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.append('y')
print(q)

from collections import defaultdict
dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])