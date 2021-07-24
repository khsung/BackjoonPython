#18111 마인크래프트
import sys
n,m,b=map(int,input().split())
graph=[]
left=0
right=0
res_time=1000000
res_height=0
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    temp_max=max(temp)
    if temp_max>right:
        right=temp_max
    graph.append(temp)

while left<=right:
    minus=0
    plus=0
    mid=(left+right)//2
    for i in range(n):
        for j in range(m):
            if graph[i][j]<mid:
                plus+=(mid-graph[i][j])
            else:
                minus+=(graph[i][j]-mid)*2
    if plus<=minus//2+b:
        if res_time>=plus+minus:
            res_time=plus+minus
            if res_height<=mid:
                res_height=mid
        left=mid+1
    else:
        right=mid-1
print(res_time,res_height)