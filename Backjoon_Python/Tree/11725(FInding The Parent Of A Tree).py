#11725 트리의 부모 찾기
n=int(input())
parent=visited=[0 for i in range(n)]
graph=[[]for j in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
visited[0]=1
queue=[]
queue.append([0,graph[0]])
while len(queue)>0:
    temp=queue.pop(0)
    pnode=temp[0]
    edgenode=temp[1]
    for i in range(len(edgenode)):
        if visited[edgenode[i]]==0:
            visited[edgenode[i]]=1
            parent[edgenode[i]]=pnode+1
            queue.append([edgenode[i],graph[edgenode[i]]])
for i in range(1,n):
    print(parent[i])