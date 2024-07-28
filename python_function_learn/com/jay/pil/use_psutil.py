import psutil
print(psutil.cpu_count()) #cpu逻辑数量
print(psutil.cpu_count(logical=False)) #cpu物理核心
# 统计CPU的用户／系统／空闲时间：空闲时间
print(psutil.cpu_times())

# 其他的参考
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000