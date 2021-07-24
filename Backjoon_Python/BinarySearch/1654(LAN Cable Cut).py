#1654 랜선 자르기
k,n=map(int,input().split())
left=1
right=0
cable=[]
res=0
for i in range(k):
    temp=int(input())
    if temp>right:
        right=temp
    cable.append(temp)

while left<=right:
    cnt=0
    mid=(left+right)//2
    for i in cable:
        cnt+=(i//mid)
    if cnt>=n:
        left=mid+1
        if mid>res:
            res=mid
    else:
        right=mid-1
print(res)