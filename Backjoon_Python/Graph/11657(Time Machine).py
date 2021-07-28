#11657 타임머신
n,m=map(int,input().split())
INF=float('inf')
edge_info=[]
cost=[INF for i in range(n)]
cost[0]=0
check=False
for i in range(m):
    a,b,c=map(int,input().split())
    edge_info.append([a-1,b-1,c])

edge_info.sort(key=lambda x:x[0])

for i in range(n):
    for j in edge_info:
        if cost[j[0]]+j[2]<cost[j[1]]:
            if i==n-1:
                check=True
                break
            else:
                cost[j[1]]=cost[j[0]]+j[2]
if check:
    print(-1)
else:
    for i in range(1,n):
        if cost[i]==INF:
            print(-1)
        else:
            print(cost[i])