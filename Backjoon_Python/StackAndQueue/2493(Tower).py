#2493 탑 
import sys
n = int(sys.stdin.readline())
tower=list(map(int,sys.stdin.readline().split()))
res=[0 for i in range(n)]
queue=[n-1]
for i in range(n-2,-1,-1):
    if len(queue)>0 and tower[i]>tower[queue[len(queue)-1]]:
        while len(queue)>0 and tower[i]>tower[queue[len(queue)-1]]:
            res[queue.pop()]=i+1
        queue.append(i)
    else:
        queue.append(i)

for i in res:
    print(i,end=" ")