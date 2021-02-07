#2525 오븐 시계
h,m=input().split()
h=int(h)
m=int(m)
time=int(input())
m+=time
cnt=0
if m>=60:
    while m>=60:
        m-=60
        cnt+=1
h+=cnt
if h>=24:
    while h>=24:
        h-=24
print(h,m)