#1697 숨바꼭질
n,k=map(int, input().split())
queue=[[n,0]]
cnt=0
res=0
visited=[0 for i in range(k*2)]
while True:
    print(queue)
    temp=queue.pop(0)
    if temp[0]==k:
        res=temp[1]
        break
    else:
        if 2*temp[0]<=k and visited[2*temp[0]]==0:
            queue.append([2*temp[0],temp[1]+1])
            visited[2*temp[0]]=1
        if temp[0]+1<=k and visited[temp[0]+1]==0:
            queue.append([temp[0]+1,temp[1]+1])
            visited[temp[0]+1]=1
        if temp[0]-1<=k and temp[0]-1>0 and visited[temp[0]-1]==0:
            queue.append([temp[0]-1,temp[1]+1])
            visited[temp[0]-1]=1
        print(temp[0]-1,k,visited[temp[0]-1])
    print("end")
print(res)
#5 3 일떄 안됨