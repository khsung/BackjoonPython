#11052 카드 구매하기
n=int(input())
card=list(map(int,input().split()))
card.insert(0,0)

dp=[0 for i in range(n+1)]
for i in range(len(dp)):
    for j in range(1,len(card)):
        if i>=j and dp[i-j]+card[j]>dp[i]:
            dp[i]=dp[i-j]+card[j]
print(dp[n])