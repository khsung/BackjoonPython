#2252 줄 세우기
from collections import deque
import sys
n,m=map(int,input().split())
adj_graph=[[]for i in range(n)]
queue=deque()
index=1
visited=[0 for i in range(n)]
for i in range(m):
    temp=list(map(int,sys.stdin.readline().split()))
    adj_graph[temp[1]-1].append(temp[0])
for i in adj_graph:
    queue.append([index,i])
    index+=1
queue=sorted(queue,key=lambda x:len(x[1]))
while len(queue)>0:
    temp=queue.pop(0)
    if len(temp[1])==0:
        print(temp[0],end=" ")
        visited[temp[0]-1]=1
    else:
        for i in temp[1]:
            if visited[i-1]==1:
                temp[1].remove(i)
        if len(temp[1])==0:
            print(temp[0],end=" ")
            visited[temp[0]-1]=1
        else:
            queue.append(temp)