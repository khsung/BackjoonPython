#2583 영역 구하기
m,n,k=map(int,input().split())
graph=[[0 for i in range(n)]for j in range(m)]
for i in range(k):
    a,b,c,d=map(int,input().split())
    for j in range(b,d):
        for k in range(a,c):
            graph[j][k]+=1

res=[]
queue=[]
dir=[[-1,0],[0,-1],[1,0],[0,1]]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            temp_cnt=0
            queue.append([i,j])
            graph[i][j]=1
            while len(queue)>0:
                temp=queue.pop(0)
                temp_cnt+=1
                for k in range(len(dir)):
                    dy=dir[k][0]+temp[0]
                    dx=dir[k][1]+temp[1]
                    if 0<=dx<n and 0<=dy<m and graph[dy][dx]==0:
                        graph[dy][dx]=1
                        queue.append([dy,dx])

            res.append(temp_cnt)
res.sort()
print(len(res))
for i in res:
    print(i,end=" ")