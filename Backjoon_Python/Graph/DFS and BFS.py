#1260 DFS와 BFS
n,m,v=input().split()
n=int(n)
m=int(m)
v=int(v)
graph=[[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a,b=input().split()
    graph[int(a)-1][int(b)-1]+=1
    graph[int(b)-1][int(a)-1]+=1
for i in range(n):
    print(graph[i])