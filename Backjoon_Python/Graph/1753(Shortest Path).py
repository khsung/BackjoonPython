#1753 최단경로 미완성
v,e=map(int,input().split())
INF=float('inf')
graph=[[INF for i in range(v)]for j in range(v)]
startnode=int(input())
path=[INF for i in range(v)]
visited=[0 for i in range(v)]
for i in range(e):
    u,v,w=map(int, input().split())
    graph[u-1][v-1]=w





for i in range(len(graph)):
    print(graph[i])
print("visited =",visited)