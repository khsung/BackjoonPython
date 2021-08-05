#1149 RGB거리
n=int(input())
color_list=[]
for i in range(n):
    temp=list(map(int,input().split()))
    color_list.append(temp)
dp=[[0,0,0]if i!=0 else color_list[0] for i in range(n)]
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+color_list[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+color_list[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+color_list[i][2]
print(min(dp[n-1]))