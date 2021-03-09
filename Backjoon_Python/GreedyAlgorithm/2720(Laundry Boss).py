#2720 세탁소 사장 동혁 합격
n=int(input())
for i in range(n):
    temp=int(input())
    cnt=0
    while temp>=25:
        temp-=25
        cnt+=1
    print(cnt,end=" ")
    cnt=0
    while temp>=10:
        temp-=10
        cnt+=1
    print(cnt,end=" ")
    cnt=0
    while temp>=5:
        temp-=5
        cnt+=1
    print(cnt,end=" ")
    cnt=0
    while temp>=1:
        temp-=1
        cnt+=1
    print(cnt)