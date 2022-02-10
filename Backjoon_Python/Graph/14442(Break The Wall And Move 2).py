#14442 벽 부수고 이동하기 2
from collections import deque
import sys
n,m,k=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

visited=[[0 for i in range(m)]for j in range(n)]
dir=[[-1,0],[1,0],[0,1],[0,-1]]

queue=deque()
            #k,i,j,cnt
queue.append([0,0,0,1])
res=-1
while len(queue)>0:
    temp=queue.popleft()
    visited[temp[1]][temp[2]]=1
    if temp[1]==n-1 and temp[2]==m-1:
        res=temp[3]
        break
    for i in range(len(dir)):
        dy=temp[1]+dir[i][0]
        dx=temp[2]+dir[i][1]
        if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0:
            if graph[dy][dx]==0:
                queue.append([temp[0],dy,dx,temp[3]+1])
            elif temp[0]+1<=k:
                queue.append([temp[0]+1,dy,dx,temp[3]+1])

print(res)