
#1929 Find Prime Number

a,b=input().split()
a=int(a)
b=int(b)
prime=[1 for i in range(b+1)]
prime[0]=0
prime[1]=0
for i in range(len(prime)):
    if prime[i]==1:
        temp=2*i
        while temp<=b:
            prime[temp]=0
            temp+=i
for i in range(a,b+1):
    if prime[i]==1:
        print(i)
