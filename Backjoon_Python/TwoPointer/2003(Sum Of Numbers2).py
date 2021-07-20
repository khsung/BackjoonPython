#2003 수들의 합 2
n,m=map(int,input().split())
array=list(map(int,input().split()))
left=-1
right=0
sum=array[0]
res=0
while right<n:
    if sum==m:
        res+=1
        right+=1
        if right<n:
            sum+=array[right]
    elif sum<m:
        right+=1
        if right<n:
            sum+=array[right]
    else:
        left+=1
        sum-=array[left]
print(res)