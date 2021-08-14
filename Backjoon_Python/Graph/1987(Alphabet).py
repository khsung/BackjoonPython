#1987 알파벳
r,c=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]
graph=[]
for i in range(r):
    graph.append(list(input()))
queue=[]
res=1
queue.append([graph[0][0],[0,0],1])
while len(queue)>0:
    path_str,curr,cnt=queue.pop()
    if cnt>res:
        res=cnt
    for i in range(4):
        x=curr[0]+dx[i]
        y=curr[1]+dy[i]
        if 0<=x<r and 0<=y<c:
            if graph[x][y] not in path_str:
                queue.append([path_str+graph[x][y],[x,y],cnt+1])
print(res)