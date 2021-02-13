#2178 미로탐색 미완성
n,m=map(int,input().split())
maze=[]
pathqueue=[]    #i,j,cnt
visited=[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    temp=list(map(int,input()))
    maze.append(temp)

