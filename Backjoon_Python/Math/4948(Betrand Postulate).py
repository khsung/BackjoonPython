#4948 베르트랑 공준
prime=[1 for i in range(246913)]
prime[0]=0
prime[1]=0
for i in range(2,len(prime)):
    if prime[i]==1:
        temp=i
        tempindex=2*temp
        while tempindex<246913:
            prime[tempindex]=0
            tempindex+=temp
while True:
    cnt=0
    a=int(input())
    if a==0:
        break
    else:
        for i in range(a+1,2*a+1):
            if prime[i]==1:
                cnt+=1
        print(cnt)