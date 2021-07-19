#16953 A -> B
A,B=map(int,input().split())
res=-1
queue=[]
queue.append([A,1])
while len(queue)>0:
    temp,cnt=queue.pop()
    if temp==B:
        res=cnt
        break
    else:
        if 10*temp+1<=B:
            queue.append([10*temp+1,cnt+1])
        if 2*temp<=B:
            queue.append([temp*2,cnt+1])
print(res)