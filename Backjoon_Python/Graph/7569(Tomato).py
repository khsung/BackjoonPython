#7569 토마토
import copy
m,n,h=map(int,input().split())
graph=[]
res=0
queue=[]
check=True
for i in range(h):
    tempgraph=[]
    for j in range(n):
        temp1=list(map(int,input().split()))
        temp=copy.deepcopy(temp1)
        tempgraph.append(temp1)
        while 1 in temp:
            queue.append([temp.index(1),j,i,0])
            temp[temp.index(1)]=0
    graph.append(tempgraph)

while len(queue)>0:
    a,b,c,cnt=queue.pop(0)      #가로,세로,높이,일자


for i in range(h):
    if check:
        for j in range(n):
            if 0 in graph[i][j]:
                check=False
                break
    else:
        break

if check:
    print(res)
else:
    print(-1)