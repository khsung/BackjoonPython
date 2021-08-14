#12851 숨바꼭질2
from collections import deque
queue=deque()
res=1000000
res_cnt=0
check=False
n,k=map(int,input().split())
visited=[0 for i in range(100001)]
if n==k:
    print(0)
else:
    queue.append([n,0])
    visited[n]=1
    while len(queue)>0:
        curr,cnt=queue.popleft()
        if cnt+1>res:
            break
        if curr-1>=0 and visited[curr-1]<=2:
            if curr-1==k:
                if res>cnt+1:
                    res=cnt+1
                    res_cnt=1
                elif res==cnt+1:
                    res_cnt+=1
                else:
                    check=True
            else:
                queue.append([curr-1,cnt+1])
                visited[curr-1]+=1
        if curr+1<=k and visited[curr+1]<=2:
            if curr+1==k:
                if res>cnt+1:
                    res=cnt+1
                    res_cnt=1
                elif res==cnt+1:
                    res_cnt+=1
                else:
                    check=True
            else:
                visited[curr+1]+=1
                queue.append([curr+1,cnt+1])

        if curr*2<=100000 and visited[curr*2]<=2:
            if curr*2==k:
                if res>cnt+1:
                    res=cnt+1
                    res_cnt=1
                elif res==cnt+1:
                    res_cnt+=1
                else:
                    check=True
            else:
                visited[curr*2]+=1
                queue.append([curr*2,cnt+1])

        if check:
            break
    print(res)
    print(res_cnt)