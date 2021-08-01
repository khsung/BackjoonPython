#6064 카잉 달력 시간 초과
test_case=int(input())

def GCD(m,n):
    if m<n:
        m,n=n,m
    if m%n==0:
        return n
    else:
        m=m%n
        return GCD(m,n)

for i in range(test_case):
    m,n,x,y=map(int,input().split())
    res=-1
    common_factor=GCD(m,n)
    temp_m=temp_n=0
    for j in range(1,n*m//common_factor+1):
        temp_m=(temp_m+1)%m
        temp_n=(temp_n+1)%n
        if temp_m==x and temp_n==y:
            res=j
            break
    print(res)