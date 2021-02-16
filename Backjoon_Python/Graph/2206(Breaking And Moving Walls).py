#2206 벽 부수고 이동하기
n,m=map(int,input().split())
square=[]
visited=[[0 for i in range(m)]for j in range(n)]
currposi=[]
res=[]
for i in range(n):
    temp=list(map(int,input()))
    square.append(temp)
currposi.append([0,0,False])
cnt=0
while len(currposi)>0:
    cnt+=1
    size=len(currposi)
    for i in range(size):
        x=currposi[0][0]
        y=currposi[0][1]
        wall=currposi[0][2]
        currposi.pop(0)
        visited[x][y]=1
        if x==n-1 and y==m-1:
            res.append(cnt)
            break
        else:
            if x-1>=0 and visited[x-1][y]==0:
                if square[x-1][y]==0:
                    currposi.append([x-1,y,wall])
                else:
                    if wall==False:
                        currposi.append([x-1,y,True])
            if y+1<m and visited[x][y+1]==0:
                if square[x][y+1]==0:
                    currposi.append([x,y+1,wall])
                else:
                    if wall==False:
                        currposi.append([x,y+1,True])
            if x+1<n and visited[x+1][y]==0:
                if square[x+1][y]==0:
                    currposi.append([x+1,y,wall])
                else:
                    if wall==False:
                        currposi.append([x+1,y,True])
            if y-1>=0 and visited[x][y-1]==0:
                if square[x][y-1]==0:
                    currposi.append([x,y-1,wall])
                else:
                    if wall==False:
                        currposi.append([x,y-1,True])
if len(res)==0:
    print(-1)
else:
    print(min(res))