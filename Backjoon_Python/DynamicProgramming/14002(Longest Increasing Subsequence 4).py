#14002 가장 긴 증가하는 부분 수열 4
n=int(input())
sequence=list(map(int,input().split()))
dp=[0 for i in range(n)]
dp[0]=1
save_index=[0 for i in range(n)]
res=[]
for i in range(1,n):
    cnt=0
    temp_index=i
    for j in range(i):
        if sequence[j]<sequence[i] and cnt<dp[j]:
            cnt=dp[j]
            temp_index=j
    dp[i]=cnt+1
    save_index[i]=temp_index
max_len=max(dp)
max_len_index=dp.index(max_len)
print(max_len)
while max_len_index != save_index[max_len_index]:
    res.append(sequence[max_len_index])
    max_len_index=save_index[max_len_index]
res.append(sequence[max_len_index])
while len(res)>0:
    print(res.pop(),end=" ")