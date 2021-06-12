#11722 가장 긴 감소하는 부분 수열
n=int(input())
sequence=list(map(int,input().split()))
dp=[0 for i in range(n)]
dp[0]=1
for i in range(1,n):
    cnt=0
    for j in range(i):
        if sequence[j]>sequence[i] and cnt<dp[j]:
            cnt=dp[j]
    dp[i]=cnt+1
print(max(dp))