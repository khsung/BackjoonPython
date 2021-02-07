#2455 지능형 기차
sum=0
max=-1
for i in range(4):
    a,b=input().split()
    a=int(a)
    b=int(b)
    sum=sum-a+b
    if max<sum:
        max=sum
print(max)
