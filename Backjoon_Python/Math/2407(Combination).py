#2407 조합
n,m=map(int,input().split())
top=bot=1
temp_n=n
temp_m=m
for i in range(m):
    top*=temp_n
    temp_n-=1
    bot*=temp_m
    temp_m-=1

print(top//bot)