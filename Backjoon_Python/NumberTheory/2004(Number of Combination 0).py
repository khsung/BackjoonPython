#2004 조합 0의 개수
n,m=input().split()
n=int(n)
m=int(m)
ncount2=0
ncount5=0
mcount2=0
mcount5=0
for i in range(m):
    temp=n
    while temp%10==0:
        ncount2+=1
        ncount5+=1
        temp=temp//10
    while temp%2==0:
        ncount2+=1
        temp=temp//2
    while temp%5==0:
        ncount5+=1
        temp=temp//5
    n-=1
    temp=m
    while temp%10==0:
        mcount2+=1
        mcount5+=1
        temp=temp//10
    while temp%2==0:
        mcount2+=1
        temp=temp//2
    while temp%5==0:
        mcount5+=1
        temp=temp//5
    m-=1
if ncount2-mcount2>ncount5-mcount5:
    print(ncount5-mcount5)
else:
    print(ncount2-mcount2)