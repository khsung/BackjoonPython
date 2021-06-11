#11053 가장 긴 증가하는 부분 수열
n=int(input())
sequence=list(map(int,input().split()))
res=[0 for i in range(n)]
res[0]=1
for i in range(1,n):
    cnt=0
    for j in range(0,i):
        if sequence[j]<sequence[i] and cnt<res[j]:
            cnt=res[j]
    res[i]=cnt+1
print(max(res))