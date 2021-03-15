#3190 뱀
n=int(input())
graph=[[0 for i in range(n)]for j in range(n)]  #1은 사과
pathdir=[]
currposition=[0,-1]
snakedir=[[0,1],[1,0],[0,-1],[-1,0]] #동,남,서,북
dirindex=0
k=int(input())
time=-1
snake=[[0,-1]]

for i in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
l=int(input())
for i in range(l):
    a,b=input().split()
    pathdir.append([int(a),b])

while True:
    time+=1
    currposition[0]+=snakedir[dirindex][0]
    currposition[1]+=snakedir[dirindex][1]
    if currposition[0]<0 or currposition[0]>n-1 or currposition[1]<0 or currposition[1]>n-1 or (currposition in snake):
        break
    else:
        tempa=currposition[0]
        tempb=currposition[1]
        snake.append([tempa,tempb])
        if graph[currposition[0]][currposition[1]]==1:
            graph[currposition[0]][currposition[1]]=0
        else:
            snake.pop(0)

        if len(pathdir)>0 and pathdir[0][0]==time:
            tempdir=pathdir[0][1]
            pathdir.pop(0)
            if tempdir=='D':
                dirindex=(dirindex+1)%4
            else:
                dirindex=(dirindex+3)%4

print(time)