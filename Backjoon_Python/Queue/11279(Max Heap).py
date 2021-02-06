#11279 최대 힙
import heapq
import sys
num=int(input())
array=[]
res=[]
for i in range(num):
    a=int(sys.stdin.readline())
    if a==0:
        if len(array)==0:
            print(0)
        else:
            print(-1*heapq.heappop(array))
    else:
        heapq.heappush(array, -a) 