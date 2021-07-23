#1644 소수의 연속합
n=int(input())
prime=[2*i+1 for i in range((n+1)//2+1)]
prime[0]=2
dp=[0]
for i in range(len(prime)):
    if prime[i]!=0:
        temp=prime[i]
        dp.append(dp[len(dp)-1]+temp)
        for j in range(i+1,len(prime)):
            if prime[j]%temp==0:
                prime[j]=0
res=0
left=0
right=1
while right<len(dp) and left<right:
    if dp[right]-dp[left]==n:
        res+=1
        left+=1
    elif dp[right]-dp[left]<n:
        right+=1
    else:
        left+=1
print(dp)
print(res)