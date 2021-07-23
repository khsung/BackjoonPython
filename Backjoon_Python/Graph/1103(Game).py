#1103 게임
from collections import deque
res=0
n,m=map(int,input().split())
graph=[]
visited=[[0 for i in range(m)]for j in range(n)]

#위, 오른쪽, 아래, 왼쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]
queue=deque()
for i in range(n):
    temp=list(input())
    graph.append(temp)
queue.append([0,0,1])
while len(queue)>0:
    x,y,cnt=queue.popleft()
    visited[x][y]=1
    if res<cnt:
        res=cnt
    check=False
    for i in range(4):
        if x+dx[i]*int(graph[x][y])>=0 and y+dy[i]*int(graph[x][y])>=0 and x+dx[i]*int(graph[x][y])<n and y+dy[i]*int(graph[x][y])<m:
            if graph[x+dx[i]*int(graph[x][y])][y+dy[i]*int(graph[x][y])]!="H":
                if visited[x+dx[i]*int(graph[x][y])][y+dy[i]*int(graph[x][y])]==1:
                    res=-1
                    check=True
                    break
                else:
                    queue.append([x+dx[i]*int(graph[x][y]),y+dy[i]*int(graph[x][y]),cnt+1])
    if check:
        break
if res==0:
    print(-1)
else:
    print(res)