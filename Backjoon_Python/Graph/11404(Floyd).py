#11404 플로이드
n=int(input())
graph=[[0 for i in range(n)]for j in range(n)]
m=int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    if graph[a-1][b-1]==0:
        graph[a-1][b-1]=c
    else:
        if graph[a-1][b-1]>c:
            graph[a-1][b-1]=c

#for i in range(len(graph)):
#    for j in range(len(graph)):
#        print(graph[i][j],end=" ")
#    print()

#print("==============")

#이부분 문제
for i in range(len(graph)):
    for j in range(len(graph)):
        for k in range(len(graph)):
            if graph[j][i]!=0 and graph[i][k]!=0 and graph[j][k]!=0 and graph[j][i]+graph[i][k]<graph[j][k]:
                print(i,j,k,graph[j][i]+graph[i][k],graph[j][k])
                graph[j][k]=graph[j][i]+graph[i][k]


print("==============")
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j],end=" ")
    print()