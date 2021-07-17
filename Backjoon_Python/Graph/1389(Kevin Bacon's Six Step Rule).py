#1389 케빈 베이컨의 6단계 법칙
from collections import deque
n,m=map(int,input().split())
graph=[[0 for i in range(n)]for j in range(n)]
min_count=5000
min_person=5000
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1
for i in range(n):
    visited=[0 for j in range(n)]
    visited[i]=1
    queue=deque()
    temp_sum=0
    queue.append([i,0])
    while len(queue)>0 and 0 in visited:
        person,cnt=queue.popleft()
        if visited[person]==0:
            visited[person]=1
            temp_sum+=cnt
        for j in range(n):
            if graph[person][j]==1:
                queue.append([j,cnt+1])
    if min_count>temp_sum:
        min_count=temp_sum
        min_person=i
print(min_person+1)