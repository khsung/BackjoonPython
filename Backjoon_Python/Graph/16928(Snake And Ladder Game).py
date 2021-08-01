#16928 뱀과 사다리 게임
from collections import deque
edge_info=[0 for i in range(101)]
n,m=map(int,input().split())
visited=[0 for i in range(101)]
visited[1]=1
for i in range(n+m):
    start,end=map(int,input().split())
    edge_info[start]=end
    
queue=deque()

if edge_info[1]==0:
    queue.append([1,0])
else:
    start=1
    while edge_info[start]!=0 and start<edge_info[start]:
        start=edge_info[start]
    queue.append([start,0])

while len(queue)>0:
    curr,cnt=queue.popleft()
    if curr==100:
        print(cnt)
        break
    elif curr>=94:
        print(cnt+1)
        break
    else:
        for i in range(1,7):
            if visited[curr+i]==0:
                if edge_info[curr+i]==0:
                    queue.append([curr+i,cnt+1])
                    visited[curr+i]=1
                elif curr+i<edge_info[curr+i]:
                    queue.append([edge_info[curr+i],cnt+1])
                    visited[curr+i]=1
                    visited[edge_info[curr+i]]=1