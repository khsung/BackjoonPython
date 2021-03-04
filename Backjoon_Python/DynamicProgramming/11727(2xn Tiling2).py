#11727 2xn 타일링 2
n=int(input())
dp=[0 for i in range(1000)]
dp[0]=1
dp[1]=2+dp[0]
index=1
if n==1 or n==2:
    print(dp[n-1])
else:
    while index<n-1:
        index+=1
        dp[index]=dp[index-1]+2*dp[index-2]
        dp[index]=dp[index]%10007
    print(dp[index])