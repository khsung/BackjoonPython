#11779 최소비용 구하기 2
import sys
INF=float('inf')
n=int(input())
m=int(input())
visited=[0 for i in range(n)]
path=[[] for i in range(n)]
cost=[[INF,[i]]for i in range(n)]
for i in range(m):
    temp=list(map(int,sys.stdin.readline().split()))
    path[temp[0]-1].append([temp[1]-1,temp[2]])

start,end=map(int,input().split())
start-=1
end-=1
visited[start]=1
cost[start][0]=0

#다익스트라 구현
for i in range(n):
    for j in range(len(path[start])):
        if cost[start][0]+path[start][j][1]<cost[path[start][j][0]][0]:
            cost[path[start][j][0]][0]=cost[start][0]+path[start][j][1]
            cost[path[start][j][0]][1]=cost[start][1]+[path[start][j][0]]
    
    temp_cost=INF
    for j in range(n):
        if visited[j]==0 and cost[j][0]<temp_cost:
            temp_cost=cost[j][0]
            start=j

    visited[start]=1

print(cost[end][0])
print(len(cost[end][1]))
for i in range(len(cost[end][1])):
    print(cost[end][1][i]+1,end=" ")