#14501 퇴사
n=int(input())
schedule=[]
max_cost=0
for i in range(n):
    schedule.append(list(map(int,input().split())))
dp=[0 for i in range(n+1)]
for i in range(n-1,-1,-1):
    if i+schedule[i][0]-1<n:
        dp[i]=max(dp[i+schedule[i][0]]+schedule[i][1],dp[i+1])
        if dp[i]>max_cost:
            max_cost=dp[i]
print(max_cost)
