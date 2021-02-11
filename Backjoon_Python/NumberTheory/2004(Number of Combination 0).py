#2004 조합 0의 개수
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
cnt=0
while first%10==0:
    cnt+=1
    first=first//10
print(cnt)
