#11404 플로이드
n=int(input())
graph=[[100001 for i in range(n)]for j in range(n)]
m=int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    if graph[a-1][b-1]==0 or graph[a-1][b-1]>c:
        graph[a-1][b-1]=c

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[i][j]+graph[j][k]<graph[i][k]:
                graph[i][k]=graph[i][j]+graph[j][k]
            if i==k:
                graph[i][k]=0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[i][j]+graph[j][k]<graph[i][k]:
                graph[i][k]=graph[i][j]+graph[j][k]
            if i==k:
                graph[i][k]=0

for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j],end=" ")
    print()