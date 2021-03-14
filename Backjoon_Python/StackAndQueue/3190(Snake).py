#3190 뱀
n=int(input())
graph=[[0 for i in range(n)]for j in range(n)]  #1은 사과, 2는 뱀의 몸통
pathdir=[]
currposition=[0,-1]
snakedir=[[0,1],[1,0],[0,-1],[-1,0]] #동,남,서,북
dirindex=0
pathdir.append(currposition)
k=int(input())
time=-1

for i in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
l=int(input())
for i in range(l):
    a,b=input().split()
    pathdir.append([int(a),b])

while True:
    time+=1



print(time)