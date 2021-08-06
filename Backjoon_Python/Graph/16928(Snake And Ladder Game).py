#16928 뱀과 사다리 게임
from collections import deque
edge_info=[0 for i in range(101)]
n,m=map(int,input().split())
visited=[0 for i in range(100)]
queue=deque()
for i in range(n+m):
    temp=list(map(int,input().split()))
    edge_info[temp[0]]=temp[1]

             #curr,cnt
queue.append([1,0])
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
            if edge_info[curr+i]==0 and visited[curr+i]==0:
                visited[curr+i]=1
                queue.append([curr+i,cnt+1])
            else:
                if visited[curr+i]==0:
                    visited[curr+i]=1
                    visited[edge_info[curr+i]]=1
                    queue.append([edge_info[curr+i],cnt+1])