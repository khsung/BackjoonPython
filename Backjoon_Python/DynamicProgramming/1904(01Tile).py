#1904 01타일
num=int(input())
dp=[0 for i in range(1000001)]
dp[1]=1
dp[2]=2
for i in range(num-2):
    dp[i+3]=(dp[i+2]+dp[i+1])%15746
print(dp[num])