#2293 동전 1
n,k=map(int,input().split())
coin=[]
dp=[0 for i in range(k+1)]
for i in range(n):
    coin.append(int(input()))

for i in range(len(dp)):
    for j in range(len(coin)):
        if i-coin[j]>=0:
            if dp[i-coin[j]]==0:
                dp[i]+=1
            else:
                dp[i]+=dp[i-coin[j]]

print(dp)
print(dp[k])