#1753 최단경로
import sys
v,e=map(int,input().split())
INF=float('inf')
edge_list=[[] for i in range(v)]
startnode=int(input())-1
cost=[INF for i in range(v)]
visited=[0 for i in range(v)]
visited[startnode]=1
cost[startnode]=0
for i in range(e):
    temp=list(map(int,sys.stdin.readline().split()))
    edge_list[temp[0]-1].append([temp[1]-1,temp[2]])

while True:
    for i in range(len(edge_list[startnode])):
        if cost[edge_list[startnode][i][0]]>edge_list[startnode][i][1]+cost[startnode]:
            cost[edge_list[startnode][i][0]]=edge_list[startnode][i][1]+cost[startnode]
    temp_index=INF
    min_cost=INF
    for i in range(v):
        if visited[i]==0 and cost[i]<min_cost:
            min_cost=cost[i]
            temp_index=i
    if temp_index==INF:
        break
    else:
        visited[temp_index]=1
        startnode=temp_index
for i in cost:
    if i==INF:
        print("INF")
    else:
        print(i)