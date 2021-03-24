#11726 2Xn 타일링
n=int(input())
dp=[0 for i in range(n+2)]
index=0
while index<=n:
    index+=1
    if index==1:
        dp[index]=1
    elif index==2:
        dp[index]=2
    else:
        dp[index]=(dp[index-1]+dp[index-2])%10007
print(dp[n])