#3055 탈출
import sys
from collections import deque
r,c=map(int,input().split())
graph=[]
water=deque()
path=deque()
dest=False
res="KAKTUS"

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#지도 생성
for i in range(r):
    temp=list(sys.stdin.readline())
    for j in range(c):
        if temp[j]=="*":
            water.append([i,j])
        elif temp[j]=="S":
            start=[i,j,0]
            path.append(start)
    graph.append(temp)


while not dest:
    water_len=len(water)
    for i in range(water_len):
        x,y=water.popleft()
        for j in range(4):
            if x+dx[j]>=0 and y+dy[j]>=0 and x+dx[j]<r and y+dy[j]<c and (graph[x+dx[j]][y+dy[j]]=="." or graph[x+dx[j]][y+dy[j]]=="S"):
                graph[x+dx[j]][y+dy[j]]="*"
                water.append([x+dx[j],y+dy[j]])
    
    path_len=len(path)
    for i in range(path_len):
        x,y,cnt=path.popleft()
        graph[x][y]="#"
        for j in range(4):
            if x+dx[j]>=0 and y+dy[j]>=0 and x+dx[j]<r and y+dy[j]<c:
                if graph[x+dx[j]][y+dy[j]]==".":
                    path.append([x+dx[j],y+dy[j],cnt+1])
                elif graph[x+dx[j]][y+dy[j]]=="D":
                    res=cnt+1
                    dest=True
                    break
    if len(path)==0:
        break
print(res)