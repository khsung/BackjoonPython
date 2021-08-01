#11403 경로 찾기
n=int(input())
graph=[]
for i in range(n):
    temp=list(map(int,input().split()))
    graph.append(temp)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k]==0:
                if graph[j][i]==1 and graph[i][k]==1:
                    graph[j][k]=1

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()