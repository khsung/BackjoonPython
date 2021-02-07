#9020 골드바흐의 추측   미완성
prime=[1 for i in range(10001)]
prime[0]=0
prime[1]=0
for i in range(2,len(prime)):
    if prime[i]==1:
        temp=i
        tempindex=2*temp
        while tempindex<=10000:
            prime[tempindex]=1
            tempindex+=temp