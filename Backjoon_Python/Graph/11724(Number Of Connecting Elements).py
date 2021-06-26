#11724 연결 요소의 개수
import sys
n,m=map(int,input().split())
graph=[[0 for i in range(n)]for j in range(n)]
visited=[0 for i in range(n)]
res=0
stack=[]

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u-1][v-1]=1
    graph[v-1][u-1]=1
for i in range(n):
    if visited[i]==0:
        res+=1
        visited[i]=1
        for j in range(n):
            if graph[i][j]==1 and visited[j]==0:
                stack.append(j)
        while len(stack)>0:
            temp_node=stack.pop()
            visited[temp_node]=1
            for j in range(n):
                if visited[j]==0 and graph[temp_node][j]==1:
                    stack.append(j)
print(res)