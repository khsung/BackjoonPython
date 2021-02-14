#7576 토마토
import copy,sys
m,n=map(int,input().split())
square=[]
visited=[[0 for i in range(m)]for j in range(n)]
tomatoinfo=[]
check=True
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    temp1=copy.deepcopy(temp)
    square.append(temp1)
    for j in range(temp.count(1)):
        tomatoinfo.append([i,temp.index(1)])
        temp[temp.index(1)]=0
cnt=0
while len(tomatoinfo)>0:
    size=len(tomatoinfo)
    for i in range(size):
        x=tomatoinfo[0][0]
        y=tomatoinfo[0][1]
        tomatoinfo.pop(0)
        if x-1>=0 and square[x-1][y]==0 and visited[x-1][y]==0:
            visited[x-1][y]=1
            square[x-1][y]=1
            tomatoinfo.append([x-1,y])
        if y+1<m and square[x][y+1]==0 and visited[x][y+1]==0:
            visited[x][y+1]=1
            square[x][y+1]=1
            tomatoinfo.append([x,y+1])
        if x+1<n and square[x+1][y]==0 and visited[x+1][y]==0:
            visited[x+1][y]=1
            square[x+1][y]=1
            tomatoinfo.append([x+1,y])
        if y-1>=0 and square[x][y-1]==0 and visited[x][y-1]==0:
            visited[x][y-1]=1
            square[x][y-1]=1
            tomatoinfo.append([x,y-1])
    if len(tomatoinfo)>0:
        cnt+=1
for i in range(n):
    if square[i].count(0)>0:      
        check=False
        break
if check==False:
    print(-1)
else:
    print(cnt)