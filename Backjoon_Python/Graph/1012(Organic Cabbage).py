#1012 유기농배추  미완성
testcase=int(input())
def bfs():

for i in range(testcase):
    m,n,k=map(int,input().split())
    graph=[[0 for i in range(m)]for j in range(n)]
    visited=[[0 for i in range(m)]for j in range(n)]
    for j in range(k):
        a,b=map(int,input().split())
        graph[b][a]+=1
    for j in range(n):
        for k in range(m):
            if

