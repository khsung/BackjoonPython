#1158 요세푸스 문제
n,k=map(int,input().split())
queue=[i+1 for i in range(n)]
index=0
print("<",end="")
while len(queue)>0:
    index+=(k-1)
    while index>n-1:
        index-=n
    print(queue[index],end="")
    del queue[index]
    n-=1
    if len(queue)>0:
        print(", ",end="")
print(">")