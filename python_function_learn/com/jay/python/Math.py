import math
def move(x,y,step,angle=0):
    nx=x+step* math.cos(angle)
    ny=y-step* math.sin(angle)
    return nx,ny

print(move(12,23,1,30))

x,y=move(100,100,60,math.pi/6)
print(x,y)

# 实际上值是放在了tuple中
r=move(100,100,60,math.pi/6)
print(r)
