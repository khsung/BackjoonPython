#1072 게임
import math
x,y=map(int,input().split())
z=math.floor((y/x)*100)
if z>=99:
    print(-1)
else:
    print(math.ceil((x*z+x-100*y)/(100-z-1)))