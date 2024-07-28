# dict中key必须是不可变对象，因为
# dict根据key来计算value的存储位置。
d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

if 'Thoms' in d:
    print('true')
else: print('false')

print('Tracy' in d)

d['Adam']=67
print(d['Adam'])

print(d.get('Tracy'))