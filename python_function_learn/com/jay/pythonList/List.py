import os
print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x*x);
print(L)

# 列表生成式
print([x*x for x in range(1,11)])


# print([d for d in os.listdir['.']])

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()]);

L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])

def uptoLower(L):
    L2=[]
    for x in  L:
        if isinstance(x,str):
            L2.append(x.lower())
        else:L2.append(x)
    return L2

print(uptoLower(['Hello', 'World', 18, 'Apple', None]))
print(isinstance(18,str))