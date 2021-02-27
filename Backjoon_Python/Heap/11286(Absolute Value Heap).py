#11286 절댓값 힙
import heapq,sys
array=[]
n=int(input())
for i in range(n):
    num=int(sys.stdin.readline())
    if num==0:
        if len(array)==0:
            print(0)
        else:
            print(heapq.heappop(array)[1])
    else:
        heapq.heappush(array, [abs(num),num])