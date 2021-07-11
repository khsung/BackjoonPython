#11660 구간 합 구하기 5
import sys
n,m=map(int,sys.stdin.readline().split())
sum_graph=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    temp.insert(0,0)
    for j in range(1,len(temp)):
        temp[j]+=temp[j-1]
    sum_graph.append(temp)
for i in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    tempsum=0
    for j in range(x1-1,x2):
        tempsum+=sum_graph[j][y2]-sum_graph[j][y1-1]
    print(tempsum)