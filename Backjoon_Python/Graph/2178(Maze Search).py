#2178 미로탐색 미완성
n,m=map(int,input().split())
maze=[]
pathqueue=[]
res=10000
visited=[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    temp=list(map(int,input()))
    maze.append(temp)

visited[0][0]=1
pathqueue.append([0,0])
cnt=1
while True: 
    pathsize=len(pathqueue)
    for i in range(pathsize):
        x=pathqueue[0][0]
        y=pathqueue[0][1]
        pathqueue.pop(0)
        if x==n-1 and y==m-1:
            if res>cnt:
                res=cnt
        else:
            if x-1>=0 and maze[x-1][y]==1 and visited[x-1][y]==0:
                visited[x-1][y]=1
                pathqueue.append([x-1,y])
            if y+1<m and maze[x][y+1]==1 and visited[x][y+1]==0:
                visited[x][y+1]=1
                pathqueue.append([x,y+1])
            if x+1<n and maze[x+1][y]==1 and visited[x+1][y]==0:
                visited[x+1][y]=1
                pathqueue.append([x+1,y])
            if y-1>=0 and maze[x][y-1]==1 and visited[x][y-1]==0:
                visited[x][y-1]=1
                pathqueue.append([x,y-1])
    if len(pathqueue)==0:
        break
    else:
        cnt+=1
print(res)
