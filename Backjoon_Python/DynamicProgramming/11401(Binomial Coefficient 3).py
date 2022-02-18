#11401 이항 계수 3
n,k=map(int,input().split())
res=1
while k>1:
    res*=n
    n-=1
    if res%k==0:
        res=res//k
        k-=1
print(res%1000000007)