#14940 쉬운 최단거리
n,m=map(int,input().split())
res_graph=[[0 for i in range(m)]for j in range(n)]
visited=[[0 for i in range(m)]for j in range(n)]
graph=[]
check=False
queue=[]
for i in range(n):
    temp=list(map(int,input().split()))
    if not check:
        if 2 in temp:
            start=[i,temp.index(2),0]
            visited[i][temp.index(2)]=1
            check=True
    graph.append(temp)
queue.append(start)

while len(queue)>0:
    i,j,cnt=queue.pop(0)
    res_graph[i][j]=cnt
    if i-1>=0 and graph[i-1][j]==1 and visited[i-1][j]==0:
        visited[i-1][j]=1
        queue.append([i-1,j,cnt+1])
    if j+1<m and graph[i][j+1]==1 and visited[i][j+1]==0:
        visited[i][j+1]=1
        queue.append([i,j+1,cnt+1])
    if i+1<n and graph[i+1][j]==1 and visited[i+1][j]==0:
        visited[i+1][j]=1
        queue.append([i+1,j,cnt+1])
    if j-1>=0 and graph[i][j-1]==1 and visited[i][j-1]==0:
        visited[i][j-1]=1
        queue.append([i,j-1,cnt+1])

#정답 출력
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and res_graph[i][j]==0:
            print(-1,end=" ")
        else:
            print(res_graph[i][j],end=" ")
    print()