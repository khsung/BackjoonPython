#9465 스티커
t=int(input())
for i in range(t):
    n=int(input())
    first=list(map(int,input().split()))
    second=list(map(int,input().split()))
    dp=[[0,0] for j in range(n+1)]
    dp[1][0]=first[0]
    dp[1][1]=second[0]
    for j in range(2,n+1):
        dp[j][0]=max(dp[j-1][1],dp[j-2][1])+first[j-1]
        dp[j][1]=max(dp[j-1][0],dp[j-2][0])+second[j-1]
    print(max(dp[n]))