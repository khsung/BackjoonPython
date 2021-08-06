#17070 파이프 옮기기 1
from collections import deque
import sys
n=int(input())
graph=[]
queue=deque()
res=0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

            #end, start
queue.append([[0,1],[0,0]])

while len(queue)>0:
    end,start=queue.popleft()
    #가로일 때
    if end[0]-start[0]==0 and end[1]-start[1]==1:
        if end[1]+1<n and graph[end[0]][end[1]+1]==0:
            if end[0]==n-1 and end[1]+1==n-1:
                res+=1
            else:
                queue.append([[end[0],end[1]+1],end])

    #세로일 때
    elif end[0]-start[0]==1 and end[1]-start[1]==0:
        if end[0]+1<n and graph[end[0]+1][end[1]]==0:
            if end[0]+1==n-1 and end[1]==n-1:
                res+=1
            else:
                queue.append([[end[0]+1,end[1]],end])

    #대각선일 때
    else:
        if end[0]+1<n and graph[end[0]+1][end[1]]==0:
            if end[0]+1==n-1 and end[1]==n-1:
                res+=1
            else:
                queue.append([[end[0]+1,end[1]],end])
        if end[1]+1<n and graph[end[0]][end[1]+1]==0:
            if end[0]==n-1 and end[1]+1==n-1:
                res+=1
            else:
                queue.append([[end[0],end[1]+1],end])
    if end[0]+1<n and end[1]+1<n and graph[end[0]+1][end[1]+1]==0 and graph[end[0]+1][end[1]]==0 and graph[end[0]][end[1]+1]==0:
            if end[0]+1==n-1 and end[1]+1==n-1:
                res+=1
            else:
                queue.append([[end[0]+1,end[1]+1],[end[0]+1,end[1]+1]])
print(res)