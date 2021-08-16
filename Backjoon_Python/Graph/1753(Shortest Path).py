#1753 최단경로
import sys
INF=float('inf')
v,e=map(int,input().split())
start=int(input())-1
visited=[0 for i in range(v)]
cost=[INF for i in range(v)]
path=[[]for j in range(v)]
cost[start]=0
visited[start]=1
for i in range(e):
    temp=list(map(int,sys.stdin.readline().split()))
    path[temp[0]-1].append([temp[1]-1,temp[2]])

for i in range(v):
    for j in range(len(path[start])):
        if path[start][j][1]+cost[start]<cost[path[start][j][0]]:
            cost[path[start][j][0]]=path[start][j][1]+cost[start]

    temp_cost=INF
    for j in range(v):
        if visited[j]==0 and cost[j]<temp_cost:
            start=j
            temp_cost=cost[j]

    visited[start]=1

for i in range(v):
    if cost[i]==INF:
        print("INF")
    else:
        print(cost[i])