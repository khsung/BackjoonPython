#1463 1로 만들기
n=int(input())
dp=[0,0]
cur=1
while cur<n:
    cur+=1
    dp.append(dp[cur-1]+1)
    if cur%2==0:
        dp[cur]=min(dp[cur],dp[cur//2]+1)
    if cur%3==0:
        dp[cur]=min(dp[cur],dp[cur//3]+1)
print(dp[cur])