#1010 다리놓기
num=int(input())
res=[]
for i in range(num):
    a,b=input().split()
    a=int(a)
    b=int(b)
    nume=1
    denom=1
    for j in range(a):
        nume*=b
        b-=1
    for j in range(a):
        denom*=a
        a-=1
    res.append(nume//denom)
for i in range(len(res)):
    print(res[i])
