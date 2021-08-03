#12851 숨바꼭질2
from collections import deque
n,k=map(int,input().split())
visited=[0 for i in range(100009)]
visited[n]=1
min_time=100009
cnt=0
queue=deque()
if n==k:
    print(0)
    print(cnt)
else:
    queue.append([n,0])
    while len(queue)>0:
        curr,curr_time=queue.popleft()
        if curr==k:
            if min_time>curr_time:
                min_time=curr_time
                cnt+=1
            elif min_time==curr_time:
                cnt+=1
            else:
                break
        else:
            if min_time!=100009 and min_time<curr_time:
                break
            else:
                if curr+1<=100000 and visited[curr+1]==0 and curr<k:
                    if curr+1!=k:
                        visited[curr+1]=1
                    queue.append([curr+1,curr_time+1])
                if curr-1>=0 and visited[curr-1]==0:
                    if curr-1!=k:
                        visited[curr-1]=1
                    queue.append([curr-1,curr_time+1])
                if 2*curr<=100000 and visited[2*curr]==0 and curr<k:
                    if 2*curr!=k:
                        visited[2*curr]=1
                    queue.append([2*curr,curr_time+1])
    print(min_time)
    print(cnt)