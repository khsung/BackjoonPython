#1012 유기농배추  시간초과
import sys
sys.setrecursionlimit(10**6)
testcase=int(input())
queue=[]
def bfs():
    global graph
    global visited
    global n
    global m
    global queue
    templen=len(queue)
    end=1
    for i in range(templen):
        tempj=queue[0][0]
        tempk=queue[0][1]
        queue.pop(0)
        if tempj-1>=0 and graph[tempj-1][tempk]==1 and visited[tempj-1][tempk]==0:
            visited[tempj-1][tempk]=1
            queue.append([tempj-1,tempk])
            end=0
        if tempk+1<m and graph[tempj][tempk+1]==1 and visited[tempj][tempk+1]==0:
            visited[tempj][tempk+1]=1
            queue.append([tempj,tempk+1])
            end=0
        if tempj+1<n and graph[tempj+1][tempk]==1 and visited[tempj+1][tempk]==0:
            visited[tempj+1][tempk]=1
            queue.append([tempj+1,tempk])
            end=0
        if tempk-1>=0 and graph[tempj][tempk-1]==1 and visited[tempj][tempk-1]==0:
            visited[tempj][tempk-1]=1
            queue.append([tempj,tempk-1])
            end=0
    if end==0:
        bfs()

for i in range(testcase):
    cnt=0
    m,n,k=map(int,input().split())
    graph=[[0 for i in range(m)]for j in range(n)]
    visited=[[0 for i in range(m)]for j in range(n)]
    for j in range(k):
        a,b=map(int,input().split())
        graph[b][a]+=1
    for j in range(n):
        for k in range(m):
            if visited[j][k]==0 and graph[j][k]==1:
                cnt+=1
                queue.append([j,k])
                bfs()
    print(cnt)

