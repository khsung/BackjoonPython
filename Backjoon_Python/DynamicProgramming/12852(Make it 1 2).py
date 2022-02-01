#12852 1로 만들기 2
n=int(input())
dp=[0 for i in range(n+1)]

for i in range(2,n+1):
    dp[i]=dp[i-1]
    if i%2==0 and dp[i//2]<dp[i]:
        dp[i]=dp[i//2]
    if i%3==0 and dp[i//3]<dp[i]:
        dp[i]=dp[i//3]
    dp[i]+=1

print(dp[n])
curr=n
while curr>0:
    print(curr,end=" ")
    if curr%2==0 and dp[curr//2]+1==dp[curr]:
        curr=curr//2
    elif curr%3==0 and dp[curr//3]+1==dp[curr]:
        curr=curr//3
    else:
        curr-=1