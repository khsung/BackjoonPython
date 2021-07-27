#1516 게임 개발
n=int(input())
indegree_list=[[] for i in range(n)]
origin_cost=[0 for i in range(n)]
cost=[0 for i in range(n)]
res=[0 for i in range(n)]
queue=[]

for i in range(n):
    temp=list(map(int,input().split()))
    origin_cost[i]=temp[0]
    for j in range(len(temp)-2):
        indegree_list[i].append(temp[j+1]-1)

for i in range(len(indegree_list)):
    if len(indegree_list[i])==0:
        queue.append(i)

while len(queue)>0:
    curr=queue.pop(0)
    res[curr]+=origin_cost[curr]
    for i in range(len(indegree_list)):
        if curr in indegree_list[i]:
            indegree_list[i].remove(curr)
            print(i,cost[i],curr,cost[curr])
            cost[i]+=origin_cost[curr]
            res[i]+=min(cost[i],origin_cost[curr])
            if len(indegree_list[i])==0:
                res[i]+=cost[curr]
                queue.append(i)
print(res)