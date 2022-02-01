#9251 LCS
first=input()
second=input()
dp=[[0 for i in range(len(second))]for j in range(len(first))]
max_cnt=[0 for i in range(len(second))]
res=0
for i in range(len(dp)):
    for j in range(len(dp[i])):
        if j<1:
            pass
        else:
            temp=max(max_cnt[:j])
            if temp>dp[i][j]:
                dp[i][j]=temp

        if first[i]==second[j]:
            dp[i][j]+=1
        if res<dp[i][j]:
            res=dp[i][j]
        if j>0 and dp[i][j]>max_cnt[j-1]:
            max_cnt[j-1]=dp[i][j]
print(res)