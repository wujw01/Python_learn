# 获取当前日期和时间
from datetime import datetime

now = datetime.now()
print(now)

# datetime 转换为timestamp
# 在计算机中，时间实际上是用数字表示的。
# 我我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
# (1970年以前的时间timestamp为负数),当前时间就是相对于
# epoch time的秒数，称为timestamp
# 可见timestamp的值与时区毫无关系，因为timestamp
# 一旦确定，其UTC时间就确定了，转换到任意时区是以timestamp表示
# 的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的。

# datetime  ---->timestamp
dt = datetime(2017, 12, 11, 11, 23)
print(dt.timestamp())
# Python的timestamp是一个浮点数，如果有小数位，小数位表示毫秒数
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
# 这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法

from datetime import datetime

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
from datetime import  datetime
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))
