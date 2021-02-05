#2606 바이러스
computer_num=int(input())
path_num=int(input())
graph = [[0 for i in range(computer_num)] for j in range(computer_num)]
for i in range(path_num):
    a,b=input().split()
    graph[int(a) - 1][int(b) - 1]+=1
    graph[int(b) - 1][int(a) - 1]+=1
nodelist = []
visited = [0 for i in range(computer_num)]
nodelist.append(0)
while len(nodelist)>0:
    tempnode=nodelist.pop(0)
    for i in range(len(graph[tempnode])):
        if graph[tempnode][i]==1 and visited[i]==0:
            nodelist.append(i)
            visited[i]=1
print(visited.count(1)-1)