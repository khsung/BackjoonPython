#1072 게임

#수학적 풀이
#import math
#x,y=map(int,input().split())
#z=(100*y)//x       파이썬의 실수오류 주의!!
#if z>=99:
#    print(-1)
#else:
#    print(math.ceil((x*z+x-100*y)/(99-z)))

x,y=map(int,input().split())
z=(100*y)//x
left=0
right=x
res=x
if z>=99:
    print(-1)
else:
    while left<=right:
        mid=(left+right)//2
        if (100*(y+mid))//(x+mid)>z:
            res=mid
            right=mid-1
        else:
            left=mid+1
    print(res)