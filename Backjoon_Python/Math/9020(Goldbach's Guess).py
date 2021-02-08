#9020 골드바흐의 추측   미완성
prime=[1 for i in range(10001)]
prime[0]=0
prime[1]=0
for i in range(2,len(prime)):
    if prime[i]==1:
        temp=i
        tempindex=2*temp
        while tempindex<=10000:
            prime[tempindex]=0
            tempindex+=temp
num=int(input())
for i in range(num):
    a=int(input())
    part_a=a//2
    part_b=a//2
    while True:
        if prime[part_a]==1 and prime[part_b]==1:
            print(part_a,part_b)
            break
        else:
            part_a-=1
            part_b+=1