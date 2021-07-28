#12738 가장 긴 증가하는 부분 수열 3
import sys
n=int(input())
num_array=list(map(int,sys.stdin.readline().split()))
res=0
dp=[0 for i in range(n)]
for i in range(n):
    cnt=0
    for j in range(i):
        if num_array[i]>num_array[j] and dp[j]>cnt:
            cnt=dp[j]
    dp[i]=cnt+1
    if res<dp[i]:
        res=dp[i]
print(res)
