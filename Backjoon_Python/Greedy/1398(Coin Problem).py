#1398 동전 문제
t=int(input())
coin=[]
temp=1
while temp<=10**15:
    coin.append(temp)
    temp=temp*10

temp=25
while temp<=10**15:
    coin.append(temp)
    temp=temp*100
coin.sort()

for i in range(t):
    cost=int(input())
    res=0
    curr_index=len(coin)-1
    while cost>0:
        res+=cost//coin[curr_index]
        cost=cost%coin[curr_index]
        curr_index-=1
    print(res)