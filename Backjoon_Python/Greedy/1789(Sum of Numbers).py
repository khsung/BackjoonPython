#1789 수들의 합
n=int(input())
res=0
temp=1
while True:
    res+=1
    n-=temp
    temp+=1
    if n<temp:
        break
print(res)