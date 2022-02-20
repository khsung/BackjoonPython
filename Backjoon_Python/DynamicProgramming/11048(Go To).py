#11048 이동하기
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if i==0:
            if j>0:
                graph[i][j]+=graph[i][j-1]
        else:
            if j==0:
                graph[i][j]+=graph[i-1][j]
            else:
                graph[i][j]+=max(graph[i-1][j],graph[i][j-1])

print(graph[n-1][m-1])