#2579 계단 오르기
n=int(input())
stair=[]
dp=[0 for i in range(n+1)]
for i in range(n):
    stair.append(int(input()))
dp[1]=stair[0]
if n>1:
    dp[2]=stair[0]+stair[1]
for i in range(3,n+1):
    dp[i]=max(stair[i-1]+stair[i-2]+dp[i-3],dp[i-2]+stair[i-1])
print(dp[n])