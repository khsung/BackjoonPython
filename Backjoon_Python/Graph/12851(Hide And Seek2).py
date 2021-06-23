#12851 숨바꼭질2
n,k=map(int, input().split())
visited=[0 for i in range(100001)]
if n==k:
    print(0)
else:
    queue=[[n,0]]
    while len(queue)>0:
        temp_n,time=queue.pop(0)
        if temp_n==k:
            cnt=1
            print(time)
            while len(queue)>0:
                temp_n2,time2=queue.pop(0)
                if time2!=time:
                    break
                elif temp_n==temp_n2:
                    cnt+=1
            break
        else:
            if temp_n-1>=0 and visited[temp_n-1]==0:
                if temp_n-1!=k:
                    visited[temp_n-1]=1
                queue.append([temp_n-1,time+1])
            if temp_n+1<=100000 and visited[temp_n+1]==0:
                if temp_n+1!=k:
                    visited[temp_n+1]=1
                queue.append([temp_n+1,time+1])
            if temp_n*2<=100000 and visited[temp_n*2]==0:
                if temp_n*2!=k:
                    visited[temp_n*2]=1
                queue.append([temp_n*2,time+1])
print(cnt)