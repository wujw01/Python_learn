import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s1 = json.dumps(obj, ensure_ascii=False)
print(s1)