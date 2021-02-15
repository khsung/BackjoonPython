#2206 벽 부수고 이동하기 미완성
n,m=map(int,input().split())
square=[]
visited=[[0 for i in range(m)]for j in range(n)]
currposi=[]
res=[5,1,2]
for i in range(n):
    temp=list(map(int,input()))
    square.append(temp)
currposi.append([0,0,False])
while len(currposi)>0:
    size=len(currposi)
    for i in range(size):
        x=currposi[0][0]
        y=currposi[0][1]
        wall=currposi[0][2]
        currposi.pop(0)
        visited[x][y]=1
        if x-1>=0 and visited[x-1][y]==0:

        if y+1<m and visited[x][y+1]==0:

        if x+1<n and visited[x+1][y]==0:

        if y-1>=0 and visited[x][y-1]==0:




if len(res)==0:
    print(-1)
else:
    print(min(res))