#18111 마인크래프트
import sys
n,m,b=map(int,input().split())
graph=[]
top_len=0
res_time=25000*600
res=0
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    if top_len<max(temp):
        top_len=max(temp)
    graph.append(temp)

while top_len>=0:
    temp_time=0
    temp_b=b
    for i in range(n):
        for j in range(m):
            temp=top_len-graph[i][j]
            if temp>=0:
                temp_time+=temp
                temp_b-=temp
            else:
                temp_time+=(-2*temp)
                temp_b-=temp
    if temp_b<0:
        top_len-=1
    else:
        if res_time>temp_time:
            res_time=temp_time
            res=top_len
            top_len-=1
        else:
            break
print(res_time,res)