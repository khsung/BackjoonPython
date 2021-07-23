#3055 탈출
r,c=map(int,input().split())
visited=[[0 for i in range(c)]for j in range(r)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
graph=[]
path=[]
check=False
res=0
for i in range(r):
    temp=list(input())
    for j in range(c):
        if temp[j]=='S':
            start=[i,j,0]
            visited[i][j]=1
            temp[j]='.'
        elif temp[j]=='*':
            path.append([i,j])
    graph.append(temp)

path.append(start)
while len(path)>0:
    temp=path.pop(0)
    for i in range(4):
        x=temp[0]+dx[i]
        y=temp[1]+dy[i]
        if x>=0 and y>=0 and x<r and y<c:
            if len(temp)==2:
                if graph[x][y]=='.':
                    graph[x][y]='*'
                    path.append([x,y])
            else:
                if visited[x][y]==0:
                    if graph[x][y]=='.':
                        path.append([x,y,temp[2]+1])
                        visited[x][y]=1
                    elif graph[x][y]=='D':
                        check=True
                        res=temp[2]+1
    if check:
        break

if check:
    print(res)
else:
    print("KAKTUS")