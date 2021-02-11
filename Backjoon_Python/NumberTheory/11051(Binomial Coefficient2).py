#11051 이항계수2
n,m=map(int,input().split())
first=second=1
tempm=m
for i in range(tempm):
    first*=n
    second*=m
    n-=1
    m-=1
    if first%second==0:
        first=first//second
        second=1
print(first%10007)