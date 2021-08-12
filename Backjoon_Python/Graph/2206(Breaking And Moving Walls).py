#2206 벽 부수고 이동하기
import sys
from collections import deque

#위,오,아,왼
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m=map(int,input().split())
graph=[]
res=-1
queue=deque()
for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))
visited=[[[0 for i in range(m)] for j in range(n)]for k in range(2)]

       #벽 부수기 전,시작위치,거리
queue.append([0,0,0,1])
visited[0][0][0]=1
while len(queue)>0:
    temp_list=queue.popleft()
    for i in range(4):
        x=temp_list[1]+dx[i]
        y=temp_list[2]+dy[i]
        if 0<=x<n and 0<=y<m:
            if x==n-1 and y==m-1:
                res=temp_list[3]+1
                break
            elif graph[x][y]==0 and visited[temp_list[0]][x][y]==0:
                visited[temp_list[0]][x][y]=1
                queue.append([temp_list[0],x,y,temp_list[3]+1])
            elif graph[x][y]==1:
                if temp_list[0]==0 and visited[0][x][y]==0:
                    visited[1][x][y]=1
                    queue.append([temp_list[0]+1,x,y,temp_list[3]+1])

    if res!=-1:
        break
if n==1 and m==1:
    print(1)
else:
    print(res)