#7569 토마토
import copy,sys
from collections import deque
m,n,h=map(int,input().split())
graph=[]
res=0
queue=deque()
check=True
for i in range(h):
    tempgraph=[]
    for j in range(n):
        temp1=list(map(int,sys.stdin.readline().split()))
        temp=copy.deepcopy(temp1)
        tempgraph.append(temp1)
        while 1 in temp:
            queue.append([temp.index(1),j,i,0])
            temp[temp.index(1)]=0
    graph.append(tempgraph)

da=[-1,1,0,0,0,0]
db=[0,0,-1,1,0,0]
dc=[0,0,0,0,-1,1]

while len(queue)>0:
    a,b,c,cnt=queue.popleft()      #가로,세로,높이,일자
    if res<cnt:
        res=cnt
    for i in range(6):
        if 0<=a+da[i] and a+da[i]<m and 0<=b+db[i] and b+db[i]<n and 0<=c+dc[i] and c+dc[i]<h and graph[c+dc[i]][b+db[i]][a+da[i]]==0:
            graph[c+dc[i]][b+db[i]][a+da[i]]=1
            queue.append([a+da[i],b+db[i],c+dc[i],cnt+1])

for i in range(h):
    if check:
        for j in range(n):
            if 0 in graph[i][j]:
                check=False
                break
    else:
        break

if check:
    print(res)
else:
    print(-1)