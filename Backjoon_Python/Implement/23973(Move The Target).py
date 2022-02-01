#23973 표적지 옮기기
n,m=map(int,input().split())
graph=[]
check=False
for i in range(n):
    graph.append(list(map(int,list(input()))))

#for i in range(len(graph)):
#    for j in range(len(graph[i])):
#        if graph[i][j]==1:
