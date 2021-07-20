#1806 부분합
n,s=map(int,input().split())
left=-1
right=0
min_len=100001
num_array=list(map(int,input().split()))
temp_sum=num_array[0]
while right<n:
    if temp_sum>=s:
        if min_len>right-left:
            min_len=right-left
        left+=1
        temp_sum-=num_array[left]
    else:
        right+=1
        if right<n:
            temp_sum+=num_array[right]
if min_len==100001:
    print(0)
else:
    print(min_len)