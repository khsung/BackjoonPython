#23741 야바위 게임
from collections import deque

n,m,x,y=map(int,input().split())
edge_check=[[0 for i in range(n)]for j in range(n)]
graph=[[] for i in range(n)]
queue=deque()
res=[]
for i in range(m):
    a,b=map(int,input().split())
    if edge_check[a-1][b-1]==0:
        edge_check[a-1][b-1]+=1
        edge_check[b-1][a-1]+=1
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

queue.append([x-1,0])

while len(queue)>0:
    curr,cnt=queue.pop()
    if cnt+1<y:
        for i in range(len(graph[curr])):
            queue.append([graph[curr][i],cnt+1])
    elif cnt+1==y:
        for i in range(len(graph[curr])):
            res.append(graph[curr][i])

if len(res)<2:
    print(-1)
else:
    res=list(set(res))
    for i in range(len(res)):
        print(res[i]+1,end=" ")


#시간초과
#from collections import deque

#n,m,x,y=map(int,input().split())
#graph=[[] for i in range(n)]
#queue=deque()
#res=[]
#for i in range(m):
#    a,b=map(int,input().split())
#    if b-1 not in graph[a-1]:
#        graph[a-1].append(b-1)
#        graph[b-1].append(a-1)

#queue.append([x-1,0])

#while len(queue)>0:
#    curr,cnt=queue.popleft()
#    if cnt+1<y:
#        for i in range(len(graph[curr])):
#            queue.append([graph[curr][i],cnt+1])
#    elif cnt+1==y:
#        for i in range(len(graph[curr])):
#            res.append(graph[curr][i])

#if len(res)<2:
#    print(-1)
#else:
#    res=list(set(res))
#    for i in range(len(res)):
#        print(res[i]+1,end=" ")