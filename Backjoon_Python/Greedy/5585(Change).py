#5585 거스름 돈
price=int(input())
price=1000-price
cnt=0
while price>=500:
    cnt+=1
    price-=500
while price>=100:
    cnt+=1
    price-=100
while price>=50:
    cnt+=1
    price-=50
while price>=10:
    cnt+=1
    price-=10
while price>=5:
    cnt+=1
    price-=5
while price>=1:
    cnt+=1
    price-=1
print(cnt)