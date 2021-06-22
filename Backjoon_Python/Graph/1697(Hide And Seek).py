#1697 숨바꼭질
n,k=map(int, input().split())
visited=[0 for i in range(100001)]
visited[n]=1
if n==k:
    print(0)
else:
    queue=[[n,0]]
    while len(queue)>0:
        temp_n,time=queue.pop(0)
        if temp_n==k:
            print(time)
            break
        else:
            if temp_n-1>=0 and visited[temp_n-1]==0:
                visited[temp_n-1]=1
                queue.append([temp_n-1,time+1])
            if temp_n+1<=100000 and visited[temp_n+1]==0:
                visited[temp_n+1]=1
                queue.append([temp_n+1,time+1])
            if temp_n*2<=100000 and visited[temp_n*2]==0:
                visited[temp_n*2]=1
                queue.append([temp_n*2,time+1])