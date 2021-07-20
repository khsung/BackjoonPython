#2805 나무 자르기
import sys
n,m=map(int,input().split())
trees=list(map(int,sys.stdin.readline().split()))
right=max(trees)
left=0
res=0
while left<=right:
    mid=(left+right)//2
    temp_sum=0
    for i in range(len(trees)):
        if trees[i]>mid:
            temp_sum+=(trees[i]-mid)
    if temp_sum>m:
        if res<mid:
            res=mid
        left=mid+1
    elif temp_sum==m:
        res=mid
        break
    else:
        right=mid-1
print(res)