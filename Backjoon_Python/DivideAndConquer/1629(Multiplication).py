#1629 곱셈
a,b,c=map(int,input().split())
digit=0
digit_list=[]
res=1
while b>0:
    if b<2**digit:
        digit_list.append(digit-1)
        b-=2**(digit-1)
        digit=0
    else:
        digit+=1
dp=[0 for i in range(digit_list[0]+1)]
dp[0]=a%c
for i in range(1,len(dp)):
    dp[i]=(dp[i-1]*dp[i-1])%c
for i in digit_list:
    res=(res*dp[i])%c
print(res)