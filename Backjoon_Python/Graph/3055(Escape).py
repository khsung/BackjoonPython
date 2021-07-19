#3055 탈출
import copy
r,c=map(int,input().split())
graph=[]
water=[]
path=[]
dest=False

#지도 생성
for i in range(r):
    temp=list(input())
    for j in range(c):
        if temp[j]=="*":
            water.append([i,j])
        elif temp[j]=="S":
            start=[i,j,0]
            path.append(start)
    graph.append(temp)

while not dest:
    temp=[]
    while len(water)>0:     #물의 이동
        a,b=water.pop()
        if a-1>=0:
            if graph[a-1][b]=='.':
                graph[a-1][b]='*'
                temp.append([a-1,b])
        if a+1<r:
            if graph[a+1][b]=='.':
                graph[a+1][b]='*'
                temp.append([a+1,b])
        if b-1>=0:
            if graph[a][b-1]=='.':
                graph[a][b-1]='*'
                temp.append([a,b-1])
        if b+1<c:
            if graph[a][b+1]=='.':
                graph[a][b+1]='*'
                temp.append([a,b+1])
    water=copy.deepcopy(temp)
    temp.clear()
    while len(path)>0:      #고슴도치 이동
        a,b,cnt=path.pop()
        tempcnt=0
        if a-1>=0:
            if graph[a-1][b]=='.':
                temp.append([a-1,b,cnt+1])
            elif graph[a-1][b]=='D':
                dest=True
                break
        if a+1<r:
            if graph[a+1][b]=='.':
                temp.append([a+1,b,cnt+1])
            elif graph[a+1][b]=='D':
                dest=True
                break
        if b-1>=0:
            if graph[a][b-1]=='.':
                temp.append([a,b-1,cnt+1])
            elif graph[a][b-1]=='D':
                dest=True
                break
        if b+1<c:
            if graph[a][b+1]=='.':
                temp.append([a,b+1,cnt+1])
            elif graph[a][b+1]=='D':
                dest=True
                break
    path=copy.deepcopy(temp)
    if dest==True:      #도착했을 경우
        print(cnt+1)
        break
    if len(path)==0 and len(water)==0:      #물과 고슴도치가 이동할 위치가 없을 때
        print("KAKTUS")
        break