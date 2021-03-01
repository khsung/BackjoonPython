#1697 숨바꼭질
n,k=map(int, input().split())
queue=[[n,0]]
cnt=0
res=0
while True:
    temp=queue.pop(0)
