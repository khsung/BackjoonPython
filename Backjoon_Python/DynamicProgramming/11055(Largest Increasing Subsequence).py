#11055 가장 큰 증가 부분 수열
n=int(input())
sequence=list(map(int,input().split()))
dp=[0 for i in range(n)]
dp[0]=sequence[0]
for i in range(1,n):
    temp_sum=0
    for j in range(i):
        if sequence[j]<sequence[i] and temp_sum<dp[j]:
            temp_sum=dp[j]
    dp[i]=temp_sum+sequence[i]
print(max(dp))