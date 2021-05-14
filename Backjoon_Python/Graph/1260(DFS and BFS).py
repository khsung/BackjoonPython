#1260 DFS와 BFS
n,m,v = input().split()
n = int(n)
m = int(m)
v = int(v)
graph = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b = input().split()
    graph[int(a) - 1][int(b) - 1]=1
    graph[int(b) - 1][int(a) - 1]=1

#dfs
visited = [0 for i in range(n)]
def dfs(start):
    global visited
    global graph
    print(start,end=" ")
    for i in range(len(graph)):
        if graph[start-1][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i+1)
visited[v-1]=1
dfs(v)
print()

#bfs
nodelist = []
visited = [0 for i in range(n)]
nodelist.append(v-1)
visited[v-1]=1
while len(nodelist)>0:
    tempnode=nodelist.pop(0)
    print(tempnode+1,end=" ")
    for i in range(len(graph[tempnode])):
        if graph[tempnode][i]==1 and visited[i]==0:
            nodelist.append(i)
            visited[i]=1
print()