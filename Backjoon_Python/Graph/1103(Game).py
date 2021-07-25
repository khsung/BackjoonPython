#1103 게임
from collections import deque
res=0
n,m=map(int,input().split())
graph=[]
visited=[[0 for i in range(m)]for j in range(n)]
visited[0][0]=1
check=False
res=1

#위, 오른쪽, 아래, 왼쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]
queue=deque()
queue.append([0,0,1])

for i in range(n):
    graph.append(list(input()))

while len(queue)>0:
    temp=queue.popleft()
    visited[temp[0]][temp[1]]=1
    for i in range(4):
        x=temp[0]+int(graph[temp[0]][temp[1]])*dx[i]
        y=temp[1]+int(graph[temp[0]][temp[1]])*dy[i]
        if x>=0 and y>=0 and x<n and y<m:
            if graph[x][y]=="H":
                break
            elif visited[x][y]==1:
                res=-1
                check=True
                break
            else:
                if res<temp[2]+1:
                    res=temp[2]+1
                queue.append([x,y,temp[2]+1])
    if check:
        break
print(res)
