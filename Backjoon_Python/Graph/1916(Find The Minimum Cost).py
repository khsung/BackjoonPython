#1916 최소비용 구하기
import sys
INF=float('inf')
n=int(input())
m=int(input())
path=[[]for i in range(n)]
cost=[INF for i in range(n)]
visited=[0 for i in range(n)]
for i in range(m):
    temp=list(map(int,sys.stdin.readline().split()))
                            #도착 지점, 비용
    path[temp[0]-1].append([temp[1]-1,temp[2]])

start,end=map(int,input().split())
start-=1
end-=1
cost[start]=0
visited[start]=1
for i in range(n):
    for j in range(len(path[start])):
        if path[start][j][1]+cost[start]<cost[path[start][j][0]]:
            cost[path[start][j][0]]=path[start][j][1]+cost[start]
    temp_cost=INF
    for j in range(n):
        if visited[j]==0 and temp_cost>cost[j]:
            temp_cost=cost[j]
            start=j
    visited[start]=1

print(cost[end])